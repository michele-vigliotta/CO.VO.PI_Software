

class Meteo():

    def __init__(self):
        super(Meteo, self).__init__()

    ''' metodo che prende come argomenti il json contenente i dati del meteo e il giorno di interesse.
        restituisce una stringa contenente i vari dati di interesse
    '''
    def get_meteo_text(self, json_data, giorno):

        cielo = json_data[giorno]['text']
        temp_max = str(json_data[giorno]['temperature_max'])
        temp_min = str(json_data[giorno]['temperature_min'])
        vento = str(json_data[giorno]['wind'])
        direzione_vento = str(json_data[giorno]['wind_direction'])
        self.testo = " " + cielo + "\n Temperature massime: " + temp_max + "°C \n Temperature minime: " \
                + temp_min + "°C \n Vento: " + vento + "km/h" + " " + direzione_vento
        return self.testo

    ''' metodo che prende come argomenti il json contenente i dati del meteo e il giorno di interesse.
            restituisce una stringa contenente il nome dell'icona che rappresenta il meteo
    '''
    def get_icona(self, json_data, giorno):

        icona = json_data[giorno]['icon']
        return icona





