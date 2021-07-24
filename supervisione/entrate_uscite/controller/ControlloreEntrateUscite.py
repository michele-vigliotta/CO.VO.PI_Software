from supervisione.entrate_uscite.model.ListaEntrateUscite import ListaEntrateUscite


class ControlloreEntrateUscite():
    def __init__(self):
        super(ControlloreEntrateUscite, self).__init__()

        self.model = ListaEntrateUscite()

    def aggiungi_entrata_uscita(self):
        return self.model.aggiungi_entrata_uscita()

    def get_lista_entrate_uscite(self):
        return self.model.get_lista_entrate_uscite()