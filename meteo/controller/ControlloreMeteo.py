from meteo.model.Meteo import Meteo

class ControlloreMeteo():

    def __init__(self):
        super(ControlloreMeteo, self).__init__()
        self.model = Meteo()

    def get_meteo_text(self, json_data, giorno):
        return self.model.get_meteo_text(json_data, giorno)

    def get_icona(self, json_data, giorno):
        return self.model.get_icona(json_data, giorno)



