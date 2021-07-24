from gestionepesca.model.GestionePesca import GestionePesca

class ControlloreGestionePesca():
    def __init__(self):
        super(ControlloreGestionePesca, self).__init__()
        self.model = GestionePesca()

    def get_barche_3(self):
        return self.model.get_barche_3()

    def get_barche_tot(self):
        return self.model.get_barche_tot()

    def get_lista_barche(self):
        return  self.model.get_lista_barche() 

