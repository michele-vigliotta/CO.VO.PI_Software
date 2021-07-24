import json
from supervisione.posizione.model.Posizione import Posizione

class ListaPosizioni():
    def __init__(self):
        super(ListaPosizioni, self).__init__()
        self.lista_posizioni = []

        with open("supervisione/data/lista_posizioni.json") as f:
            lista_posizioni_iniziali = json.load(f)
        for posizione_json in lista_posizioni_iniziali:
            self.aggiungi_posizione(Posizione(posizione_json["targa"], posizione_json["latitudine"], posizione_json["longitudine"]))
    # carica dal file json la lista delle posizioni delle barche e aggiunge le barche alla lista
    # come oggetti con modello Posizione

    def aggiungi_posizione(self, posizione):
        self.lista_posizioni.append(posizione)
    # aggiunge alla lista le posizoni delle barche passate come argomento

    def get_lista_posizioni(self):
        return self.lista_posizioni
    # restituisce la lista delle posizioni
