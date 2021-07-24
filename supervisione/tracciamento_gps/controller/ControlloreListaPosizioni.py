from supervisione.tracciamento_gps.model.ListaPosizioni import ListaPosizioni


class ControlloreListaPosizioni():
    def __init__(self):
        super(ControlloreListaPosizioni, self).__init__()

        self.model = ListaPosizioni()

    def aggiungi_posizione(self):
        return self.model.aggiungi_posizione()

    def get_lista_posizioni(self):
        return self.model.get_lista_posizioni()