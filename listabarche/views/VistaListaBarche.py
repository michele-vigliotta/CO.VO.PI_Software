from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QGridLayout, QLabel

from barca.views.VistaBarca import VistaBarca
from listabarche.controller.ControlloreListaBarche import ControlloreListaBarche
from listabarche.views.VistaInserisciBarca import VistaInserisciBarca


class VistaListaBarche(QWidget):
    def __init__(self, parent=None):
        super(VistaListaBarche, self).__init__(parent)

        self.controller = ControlloreListaBarche()

        self.list_view = QListView()
        self.list_view.setStyleSheet('background-color:white')
        self.update_ui()

        open_button = QPushButton('Apri')
        font_open_button = open_button.font()
        font_open_button.setPointSize(12)
        open_button.setFont(font_open_button)
        open_button.setStyleSheet('background-color:white;color:#ff8000')
        open_button.setIcon(QIcon('icone/apri.png'))
        open_button.setIconSize(QSize(40, 40))

        open_button.clicked.connect(self.show_selected_info)


        new_button = QPushButton("Nuovo")
        font_new_button = new_button.font()
        font_new_button.setPointSize(12)
        new_button.setFont(font_new_button)
        new_button.setStyleSheet('background-color:white;color:#ff8000')
        new_button.setIcon(QIcon('icone/nuovo.png'))
        new_button.setIconSize(QSize(60, 60))
        new_button.clicked.connect(self.show_new_barca)

        label = QLabel()

        v_layout = QVBoxLayout()
        v_layout.addWidget(new_button)
        v_layout.addWidget(label)

        g_layout = QGridLayout()
        g_layout.addWidget(self.list_view, 0, 0)
        g_layout.addLayout(v_layout, 0, 1)
        g_layout.addWidget(open_button, 1, 0)

        self.setLayout(g_layout)
        self.resize(400, 300)
        self.setWindowTitle('Gestione Barche')
        self.setStyleSheet('background-color:lightblue')
        self.setWindowIcon(QIcon('icone/gestionebarche.png'))

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for barca in self.controller.get_lista_barche():
            item = QStandardItem()
            item.setText(barca.nome + " - " + barca.targa)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(14)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def show_selected_info(self):
        if(len(self.list_view.selectedIndexes()) > 0):
            selected = self.list_view.selectedIndexes()[0].row()
            barca_selezionato = self.controller.get_barca_by_index(selected)
            self.vista_barca = VistaBarca(barca_selezionato, self.controller.elimina_barca_by_targa, self.update_ui)
            self.vista_barca.show()

    def show_new_barca(self):
        self.vista_inserisci_barca = VistaInserisciBarca(self.controller, self.update_ui)
        self.vista_inserisci_barca.show()

    def closeEvent(self, event):
        self.controller.save_data()
