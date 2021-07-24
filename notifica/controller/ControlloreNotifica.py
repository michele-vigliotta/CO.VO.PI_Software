from notifica.model.Notifica import Notifica



class ControlloreNotifica():

    def __init__(self):
        super(ControlloreNotifica, self).__init__()
        self.model = Notifica()

    def invia_messaggio(self, messaggio):
        return self.model.invia_messaggio(messaggio)