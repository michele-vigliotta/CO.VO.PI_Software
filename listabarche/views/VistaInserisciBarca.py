from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from barca.model.Barca import Barca


class VistaInserisciBarca(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciBarca, self).__init__()
        self.controller = controller
        self.callback = callback

        self.v_layout = QVBoxLayout()
        self.qlines = {}
        self.add_info_text("nome", "Nome")
        self.add_info_text("targa", "Targa")
        self.add_info_text("nomereferente", "Nome Referente")
        self.add_info_text("cognomereferente", "Cognome Referente")
        self.add_info_text("cf", "Codice Fiscale")
        self.add_info_text("telefono", "Telefono")
        self.add_info_text("equipaggio", "Equipaggio")
        self.add_info_text("licenza", "Licenza")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        font_btn_ok = btn_ok.font()
        font_btn_ok.setPointSize(12)
        btn_ok.setFont(font_btn_ok)
        btn_ok.setStyleSheet('background-color:white;color:#ff8000')
        btn_ok.clicked.connect(self.add_barca)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuova Barca")
        self.setStyleSheet('background-color:lightblue')
        self.setWindowIcon(QIcon('icone/nuovo.png'))

    def add_info_text(self, nome, label):
        text_label = QLabel(label)
        font_text_label = text_label.font()
        font_text_label.setPointSize(12)
        text_label.setFont(font_text_label)
        text_label.setStyleSheet('color:#000dc3')
        self.v_layout.addWidget(text_label)
        current_text = QLineEdit(self)
        current_text.setStyleSheet('background-color:white')
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def add_barca(self):
        for value in self.qlines.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.', QMessageBox.Ok, QMessageBox.Ok)
                return
        self.controller.aggiungi_barca(Barca(
            self.qlines["nome"].text(),
            self.qlines["targa"].text().upper(),
            self.qlines["nomereferente"].text(),
            self.qlines["cognomereferente"].text(),
            self.qlines["cf"].text(),
            self.qlines["telefono"].text(),
            self.qlines["equipaggio"].text(),
            self.qlines["licenza"].text())
        )
        self.callback()
        self.close()
