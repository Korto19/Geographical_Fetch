# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Fetch
                                 A QGIS plugin
 Generate gegraphical fetch
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-04-25
        copyright            : (C) 2022 by Giulio Fattori
        email                : giulio.fattori@tin.it
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Fetch class from file Fetch.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Fetch import Fetch
    return Fetch(iface)
