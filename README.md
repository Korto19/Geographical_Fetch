# Geographical_Fetch
Plugin per generare fetch geografici
![rosa](https://user-images.githubusercontent.com/36882050/165111355-ed7dca6a-fcd1-4b98-ad0f-ee12e920eb03.png)
Il fetch indica la superficie di mare aperto su cui spira il vento con direzione e intensità costante ed entro cui avviene la generazione del moto ondoso. Il termine fetch viene utilizzato in geografia, meteorologia, nelle costruzioni marittime ed è generalmente associato con l'erosione costiera.(fonte Wikipedia)

Il plugin genera delle rose di angolo e raggio definibili che successivamente possono essere tagliate con un poligono rappresentante l'area interessata.

Al lancio il puntatore diviene una crocetta e permette la digitalizzazione del punto di interesse, successivamente vengono richiesti raggio della rosa in m e angolo di suddivisione in gradi.

![Raggio](https://user-images.githubusercontent.com/36882050/165113148-79290ab6-6a0d-48f4-92a4-1758456bc3a6.png)
![Suddivisione](https://user-images.githubusercontent.com/36882050/165113161-e58a2752-14f5-4064-af40-e3a2b6800802.png)

Sono ammessi gradi con un solo decimale.

Al termine occorre fare click col tasto destro del mouse per terminare la procedura.

Ogni rosa generata è posta su di un diverso layer temporaneo.

Il taglio con il poligono dell'area interessata determina la grandezza risultante delle etichette.

![fetch](https://user-images.githubusercontent.com/36882050/165114210-4feb5618-bbb2-4b70-a43e-bb97c6b5a796.png)

Per modificare la grandezza delle etichette agire sugli stili già impostati
