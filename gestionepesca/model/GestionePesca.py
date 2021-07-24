import os
import pickle

class GestionePesca():
    def __init__(self):
        super(GestionePesca, self).__init__()
        self.lista_barche = []
        if os.path.isfile('listabarche/data/lista_barche_salvata.pickle'):          #se c'è, apro la lista creata in gestionebarche
            with open('listabarche/data/lista_barche_salvata.pickle', 'rb') as f:
                self.lista_barche = pickle.load(f)

    # metodo che restituisce il numero totale di barche con tre membri
    def get_barche_3(self):
        j = 0
        for barca in self.lista_barche:
            if int(barca.equipaggio) == 3:
                j += 1
        return j

    # metodo che restituisce il numero totale di barche
    def get_barche_tot(self):
        return len(self.lista_barche)

    # metodo che restituisce la lista delle barche
    def get_lista_barche(self):
        return self.lista_barche


















