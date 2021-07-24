from listabarche.model.ListaBarche import ListaBarche


class ControlloreListaBarche():
    def __init__(self):
        super(ControlloreListaBarche, self).__init__()
        self.model = ListaBarche()

    def aggiungi_barca(self, barca):
        self.model.aggiungi_barca(barca)

    def get_lista_barche(self):
        return self.model.get_lista_barche()

    def get_barca_by_index(self, index):
        return self.model.get_barca_by_index(index)

    def elimina_barca_by_targa(self, targa):
        self.model.rimuovi_barca_by_targa(targa)

    def save_data(self):
        self.model.save_data()
