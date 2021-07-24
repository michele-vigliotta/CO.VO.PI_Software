class ControlloreBarca():
    def __init__(self, barca):
        self.model = barca

    def get_nome_barca(self):
        return self.model.nome

    def get_targa_barca(self):
        return self.model.targa

    def get_nomereferente_barca(self):
        return self.model.nomereferente

    def get_cognomereferente_barca(self):
        return self.model.cognomereferente

    def get_cf_barca(self):
        return self.model.cf

    def get_telefono_barca(self):
        return self.model.telefono

    def get_equipaggio_barca(self):
        return self.model.equipaggio

    def get_licenza_barca(self):
        return self.model.licenza
