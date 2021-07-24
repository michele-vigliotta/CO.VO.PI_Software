from supervisione.entrate_uscite.model.EntrataUscita import EntrataUscita
import json


class ListaEntrateUscite():
    def __init__(self):
        super(ListaEntrateUscite, self).__init__()
        self.lista_entrate_uscite = []

        with open("Supervisione/data/lista_entrate_uscite.json") as f:
            lista_entrate_uscite_iniziali = json.load(f)
        for entr_usc_json in lista_entrate_uscite_iniziali:
            self.aggiungi_entrata_uscita(EntrataUscita(entr_usc_json["targa"], entr_usc_json["uscita"], entr_usc_json["ingresso"]))
    # carica la lista delle barche dal file json e la aggiunge nella lista lista_entrate_uscite
    # come oggetti con modello EntrataUscita

    def aggiungi_entrata_uscita(self, entrata_uscita):
        self.lista_entrate_uscite.append(entrata_uscita)
    # aggiunge nella lista le entrate e uscite passate come argomento

    def get_lista_entrate_uscite(self):
        return self.lista_entrate_uscite
    # restituisce la lista
