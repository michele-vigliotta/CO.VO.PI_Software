from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QSizePolicy, QSpacerItem, QTextEdit


from meteo.views.VistaMeteo import VistaMeteo


class VistaAccessoMeteo(QDialog):
    def __init__(self, parent=None):
        super(VistaAccessoMeteo, self).__init__(parent)

        self.icona = QLabel()
        self.icona.setPixmap(QPixmap('icone/chiave.png'))

        self.label = QLabel('Attenzione')
        self.label.setStyleSheet('color:#000dc3')
        font_label = self.label.font()
        font_label.setPointSize(12)
        self.label.setFont(font_label)

        self.text_credenziali = QTextEdit()
        self.text_credenziali.setStyleSheet('background-color:white')
        font_credenziali = self.text_credenziali.font()
        font_credenziali.setPointSize(11)
        self.text_credenziali.setFont(font_credenziali)
        self.text_credenziali.setReadOnly(True)
        self.text_credenziali.setText('Per visualizzare il meteo, assicurarsi di aver effettuato il login presso il sito:\n\nhttps://api.tutiempo.net/it/\n\nEmail :  uusep@hi2.in\n\nPassword : meteo')

        self.button_prosegui = QPushButton('Prosegui', self)
        self.button_prosegui.setStyleSheet('background-color:white ; color:#ff8000')
        button_prosegui_font = self.button_prosegui.font()
        button_prosegui_font.setPointSize(12)
        self.button_prosegui.setFont(button_prosegui_font)
        self.button_prosegui.clicked.connect(self.go_to_meteo)

        g_layout = QVBoxLayout()
        g_layout.addWidget(self.icona)
        g_layout.addWidget(self.label)
        g_layout.addWidget(self.text_credenziali)
        g_layout.addWidget(self.button_prosegui)

        g_layout.addItem(QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(g_layout)
        self.setWindowIcon(QIcon('icone/chiave.png'))
        self.setWindowTitle("Meteo")
        self.setStyleSheet('background-color:lightblue')
        x = self.width()
        y = self.height()
        self.setFixedHeight(520)
        self.setFixedWidth(290)

    def go_to_meteo(self):
        self.vista_meteo = VistaMeteo()
        self.vista_meteo.show()



