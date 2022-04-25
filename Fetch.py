# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Fetch
                                 A QGIS plugin
 Generate gegraphical fetch
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2022-04-25
        git sha              : $Format:%H$
        copyright            : (C) 2022 by Giulio Fattori
        email                : giulio.fattori@tin.it
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QInputDialog

from qgis.gui import QgsMapTool
from qgis.utils import iface
from qgis.core import QgsVectorLayer, QgsFeature, QgsPoint, QgsGeometry, QgsProject

# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
#from .Fetch_dialog import Fetch_Dialog
import os.path

import inspect
cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

import math

class Fetch:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'Fetch_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Fetch')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('Fetch', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/Fetch/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Fetch'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Fetch'),
                action)
            self.iface.removeToolBarIcon(action)


    def run(self):
        """Run method that performs all the real work"""

        class MapTool(QgsMapTool):
            def __init__(self, iface, canvas):
                super(MapTool, self).__init__(canvas)

            def canvasReleaseEvent(self, event):
                if event.button() == 1:
                    point = self.toMapCoordinates(event.pos())
                    line_rose(point)
                else:
                    print('finish')
                    iface.mapCanvas().unsetMapTool(tool)
                    
        def line_rose(point):
            v_layer = QgsVectorLayer('LineString?crs=epsg:32632', 'Fetch_line', 'memory')
            pr = v_layer.dataProvider()
            seg = QgsFeature()
            
            start_point = QgsPoint(point.x(), point.y())
            
            t_input = QInputDialog.getDouble(None, 'Raggio m ', 'Inserire lunghezza raggio m',100000.0)
            ray =(t_input[0])
            print(ray)

            t_input = QInputDialog.getDouble(None, 'Suddivisione ° ', 'Inserire angolo di suddivisione °',22.5)
            a_set =(t_input[0])
            print(a_set)
           
            if not a_set.is_integer():
                a_num = int(10)
                a_rot = int(360 * a_num)
                a_set = int(a_set * a_num)
            else:
                a_num = int(1)
                a_rot = int(360)
                a_set = int(a_set)
            
            wind_rose = [round(x/a_num,1) for x in range(0,a_rot,a_set)]
            for i in wind_rose:
                end_point = QgsPoint(start_point.x()+ray*math.cos(math.radians(i)), start_point.y()+ray*math.sin(math.radians(i)))
                seg.setGeometry(QgsGeometry.fromPolyline([start_point, end_point]))
                pr.addFeatures([ seg ])

            QgsProject.instance().addMapLayers([v_layer])
            v_layer.loadNamedStyle(os.path.join(os.path.join(cmd_folder, 'Fetch_km_lenghtdriven.qml')))
            iface.zoomToActiveLayer()
            
        tool=MapTool(iface, iface.mapCanvas())
        iface.mapCanvas().setMapTool(tool)

