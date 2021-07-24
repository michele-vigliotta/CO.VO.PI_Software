from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton
from supervisione.tracciamento_gps.views.VistaTracciamento import VistaTracciamento
from supervisione.entrate_uscite.views.VistaEntrateUscite import VistaEntrateUscite
from supervisione.violazioni.views.VistaListaViolazioni import VistaListaViolazioni


class VistaSupervisione(QWidget):
    def __init__(self, parent=None):
        super(VistaSupervisione, self).__init__(parent)
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_generic_button("Tracciamento GPS", self.go_tracciamento, "icone/icona_gps"), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Visualizza entrate e uscite", self.go_entrate_uscite, "icone/icona_entrate_uscite"), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Visualizza violazioni", self.go_violazioni, "icone/icona_violazioni.png"), 2, 0)
        grid_layout.setContentsMargins(30, 30, 30, 30)
        grid_layout.setSpacing(30)

        self.setLayout(grid_layout)
        self.resize(400, 500)
        self.setWindowTitle("Supervisione")
        self.setStyleSheet('background-color: lightblue;')
        self.setWindowIcon(QIcon("icone/supervisione.png"))

    def go_tracciamento(self):
        self.tracciamento = VistaTracciamento()
        self.tracciamento.show()
    # richiama la view del tracciamento gps

    def go_entrate_uscite(self):
        self.entrate_uscite = VistaEntrateUscite()
        self.entrate_uscite.show()
    # richiama la view delle entrate e uscite

    def go_violazioni(self):
        self.violazioni = VistaListaViolazioni()
        self.violazioni.show()
    # richiama la view della lista violazioni

    def get_generic_button(self, titolo, on_click, icona):
        button = QPushButton(titolo)
        button.setFont(QFont('Times', 14))
        button.setMinimumSize(120, 120)
        button.setStyleSheet('background-color:white;color:#ff8000')
        button.setIcon(QIcon(icona))
        button.setIconSize(QSize(50, 50))
        button.clicked.connect(on_click)
        return button
    # genera un bottone generico
