from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit, QGridLayout, QFrame, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from meteo.controller.ControlloreMeteo import ControlloreMeteo
import requests


class VistaMeteo(QWidget):

    def __init__(self):
        super(VistaMeteo, self).__init__()

        self.api_key = 'zCTz4a4q4zaBV5Q'
        self.api_1 = 'https://api.tutiempo.net/json/?lan=it&apid='+self.api_key+'&lid=95767'
        self.api_2 = 'https://api.tutiempo.net/json/?lan=it&apid='+self.api_key+'&lid=95296'



        self.json_data_1 = requests.get(self.api_1).json()  #chiamata api San Benedetto Del Tronto
        self.json_data_2 = requests.get(self.api_2).json()  #chiamata api San Benedetto Del Tronto

        self.controller = ControlloreMeteo()

        line = QFrame()
        line.setGeometry(0, 0, 50, 200)
        line.setFrameShape(QFrame.VLine)
        line.setStyleSheet('color:#ff8000')

        v1_layout = QVBoxLayout()
        v1_layout.setAlignment(Qt.AlignCenter)

        label1_larghezza = QLabel()
        label1_larghezza.resize(350, 20)
        label1_larghezza.setAlignment(Qt.AlignCenter)

        v1_layout.addWidget(self.get_generic_label('San Benedetto Del Tronto'))
        v1_layout.addWidget(self.get_generic_label('Oggi'))
        v1_layout.addWidget(self.get_generic_icon(self.json_data_1, 'day1'))
        v1_layout.addWidget(self.get_generic_text(self.json_data_1, 'day1'))
        v1_layout.addWidget(self.get_generic_label('Domani'))
        v1_layout.addWidget(self.get_generic_icon(self.json_data_1, 'day2'))
        v1_layout.addWidget(self.get_generic_text(self.json_data_1, 'day2'))
        v1_layout.addWidget(label1_larghezza)

        v2_layout = QVBoxLayout()
        v2_layout.setAlignment(Qt.AlignCenter)

        label2_larghezza = QLabel()
        label2_larghezza.resize(350, 20)
        label2_larghezza.setAlignment(Qt.AlignCenter)

        v2_layout.addWidget(self.get_generic_label('Porto San Giorgio'))
        v2_layout.addWidget(self.get_generic_label('Oggi'))
        v2_layout.addWidget(self.get_generic_icon(self.json_data_2, 'day1'))
        v2_layout.addWidget(self.get_generic_text(self.json_data_2, 'day1'))
        v2_layout.addWidget(self.get_generic_label('Domani'))
        v2_layout.addWidget(self.get_generic_icon(self.json_data_2, 'day2'))
        v2_layout.addWidget(self.get_generic_text(self.json_data_2, 'day2'))
        v2_layout.addWidget(label2_larghezza)

        v3_layout = QVBoxLayout()
        v3_layout.addWidget(line)

        h_layout = QHBoxLayout()
        h_layout.addLayout(v1_layout)
        h_layout.addLayout(v3_layout)
        h_layout.addLayout(v2_layout)

        self.setFixedSize(700, 520)
        self.setWindowTitle("Meteo")
        self.setStyleSheet('background-color:lightblue')
        self.setWindowIcon(QIcon('icone/meteo.png'))
        self.setLayout(h_layout)

    def get_generic_label(self, text):
        label = QLabel(text)
        if text != 'Oggi' and text != 'Domani':
            font = label.font()
            font.setPointSize(17)
            label.setFont(font)
            label.setStyleSheet('color:#000dc3')
        else:
            font = label.font()
            font.setPointSize(12)
            label.setFont(font)
            label.setStyleSheet('color:#ff8000')
        return label

    def get_generic_text(self, json_data, giorno):
        text = QTextEdit()
        text.setReadOnly(True)

        font = text.font()
        font.setPointSize(11)
        text.setFont(font)
        text.setStyleSheet("background-color:white")
        text.setFixedSize(215, 90)
        text.setText(self.controller.get_meteo_text(json_data, giorno))
        return text

    # metodo che presi in imput il json del meteo e il giorno di interesse,
    # setta l'icona che rappresenta le condizioni del tempo
    def get_generic_icon(self, json_data, giorno):
        icona = QLabel()
        icona.setPixmap(QPixmap('icone/'+self.controller.get_icona(json_data, giorno)+'.png'))
        return icona
