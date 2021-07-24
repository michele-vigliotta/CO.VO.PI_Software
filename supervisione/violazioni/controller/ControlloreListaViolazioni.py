from supervisione.violazioni.model.ListaViolazioni import ListaViolazioni


class ControlloreListaViolazioni():
    def __init__(self):
        super(ControlloreListaViolazioni, self).__init__()

        self.model = ListaViolazioni()

    def aggiungi_violazione(self):
        return self.model.aggiungi_violazione()

    def get_lista_violazioni(self):
        return self.model.get_lista_violazioni()