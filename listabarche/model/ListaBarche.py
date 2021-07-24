import os
import pickle


class ListaBarche():
    def __init__(self):
        super(ListaBarche, self).__init__()
        self.lista_barche = []
        if os.path.isfile('listabarche/data/lista_barche_salvata.pickle'):                  #se c'e'¨, apro la lista creata in gestionebarche
            with open('listabarche/data/lista_barche_salvata.pickle', 'rb') as f:
                self.lista_barche = pickle.load(f)

    def aggiungi_barca(self, barca):
        self.lista_barche.append(barca)

    def rimuovi_barca_by_targa(self, targa):
        def is_selected_barca(barca):
            if barca.targa == targa:
                return True
            return False
        self.lista_barche.remove(list(filter(is_selected_barca, self.lista_barche))[0])

    def get_barca_by_index(self, index):
        return self.lista_barche[index]

    def get_lista_barche(self):
        return self.lista_barche

    def save_data(self):
        with open('listabarche/data/lista_barche_salvata.pickle', 'wb') as handle:          #salvo o creo file .pickle
            pickle.dump(self.lista_barche, handle, pickle.HIGHEST_PROTOCOL)
