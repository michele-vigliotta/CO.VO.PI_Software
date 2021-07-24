from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtCore import QSize

from supervisione.view.VistaSupervisione import VistaSupervisione
from listabarche.views.VistaListaBarche import VistaListaBarche
from gestionepesca.views.VistaGestionePesca import VistaGestionePesca
from meteo.views.VistaAccessoMeteo import VistaAccessoMeteo


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)

        grid_layout = QGridLayout()
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        self.icona = QLabel()
        self.pixmap = QPixmap("icone/iconasoftware.png")
        self.icona.setPixmap(self.pixmap)
        self.icona.setMaximumSize(125, 125)
        self.spazio_1 = QLabel()
        self.spazio_2 = QLabel()

        grid_layout.addWidget(self.get_generic_button("Gestione barche", self.go_gestione_barche, "icone/gestionebarche.png"), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Meteo", self.go_meteo, "icone/meteo.png"), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Gestione pesca", self.go_gestione_pesca, "icone/gestionepesca.png"), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Supervisione", self.go_supervisione, "icone/supervisione.png"), 1, 1)
        grid_layout.setSpacing(15)
        h_layout.addWidget(self.spazio_1)
        h_layout.addWidget(self.icona)
        h_layout.addWidget(self.spazio_2)
        v_layout.addLayout(h_layout)
        v_layout.addLayout(grid_layout)
        v_layout.setContentsMargins(20, 20, 20, 20)
        v_layout.setSpacing(30)

        self.setLayout(v_layout)
        self.resize(600, 400)
        self.setWindowTitle("CO.VO.PI. Software")
        self.setStyleSheet('background-color: lightblue;')
        self.setWindowIcon(QIcon('icone/iconasoftware.png'))

    def get_generic_button(self, titolo, on_click, icona):
        button = QPushButton(titolo)
        button.setFont(QFont('Times', 16))
        button.setMinimumSize(250, 150)
        button.setStyleSheet('background-color:white;color:#ff8000')
        button.setIcon(QIcon(icona))
        button.setIconSize(QSize(60, 60))
        button.clicked.connect(on_click)
        return button

    def go_gestione_barche(self):
        self.vista_gestione_barche = VistaListaBarche()
        self.vista_gestione_barche.show()

    def go_meteo(self):
        self.vista_meteo = VistaAccessoMeteo()
        self.vista_meteo.show()
        pass

    def go_gestione_pesca(self):
        self.vista_gestione_pesca = VistaGestionePesca()
        self.vista_gestione_pesca.show()

    def go_supervisione(self):
        pass
        self.vista_supervisione = VistaSupervisione()
        self.vista_supervisione.show()


