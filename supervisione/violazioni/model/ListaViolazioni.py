from supervisione.violazioni.model.Violazione import Violazione
import json


class ListaViolazioni():
    def __init__(self):
        super(ListaViolazioni, self).__init__()
        self.lista_violazioni = []

        self.lat_max = 43.293
        self.lat_min = 42.894
        self.long_max = 14.044
        self.long_min = 13.730

        with open("supervisione/data/lista_posizioni.json") as f:
            lista_violazioni_iniziali = json.load(f)
        for violazione_json in lista_violazioni_iniziali:
           if float(violazione_json["latitudine"]) <= self.lat_min or float(violazione_json["latitudine"]) >= self.lat_max \
                    or float(violazione_json["longitudine"]) <= self.long_min or float(violazione_json["longitudine"]) >= self.long_max:

            self.aggiungi_violazione(Violazione(violazione_json["targa"], violazione_json["latitudine"], violazione_json["longitudine"]))
        # carica dal file json la lista delle barche, le aggiunge nella lista come oggetti con modello Violazione

    def aggiungi_violazione(self, violazione):
        self.lista_violazioni.append(violazione)
    # aggiunge alla lista la violazione

    def get_lista_violazioni(self):
        return self.lista_violazioni
    # restituisce la lista

