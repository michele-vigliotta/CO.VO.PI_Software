from PyQt5.QtWidgets import QDialog, QLabel, QGridLayout, QListView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from supervisione.tracciamento_gps.controller.ControlloreListaPosizioni import ControlloreListaPosizioni

class VistaTracciamento(QDialog):
    def __init__(self, parent=None):
        super(VistaTracciamento, self).__init__(parent)

        self.controller = ControlloreListaPosizioni()

        h_layout = QGridLayout()

        self.titolo_1 = QLabel("Imbarcazioni")
        self.titolo_1.setStyleSheet('color:#000dc3')
        font_label = self.titolo_1.font()
        font_label.setPointSize(14)
        self.titolo_1.setFont(font_label)
        self.titolo_2 = QLabel("     Posizione attuale")
        self.titolo_2.setStyleSheet('color:#000dc3')
        font_label = self.titolo_2.font()
        font_label.setPointSize(14)
        self.titolo_2.setFont(font_label)

        self.list_view_1 = QListView()
        self.list_view_1.setStyleSheet("Background-color: white")
        self.list_view_1.setMaximumWidth(120)
        self.list_view_2 = QListView()
        self.list_view_2.setStyleSheet("Background-color: white")

        self.update_ui_1()
        self.update_ui_2()

        h_layout.addWidget(self.titolo_1, 0, 0)
        h_layout.addWidget(self.titolo_2, 0, 1)
        h_layout.addWidget(self.list_view_1, 1, 0)
        h_layout.addWidget(self.list_view_2, 1, 1)

        self.setLayout(h_layout)
        self.resize(400, 400)
        self.setWindowTitle("Tracciamento GPS")
        self.setStyleSheet("Background-color: lightblue")
        self.setContentsMargins(10, 10, 10, 10)
        self.setWindowIcon(QIcon('icone/icona_gps.png'))

    def update_ui_1(self):
        self.listview_model_1 = QStandardItemModel(self.list_view_1)
        for posizione in self.controller.get_lista_posizioni():
            item = QStandardItem()
            item.setText(posizione.targa)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(12)
            item.setFont(font)
            self.listview_model_1.appendRow(item)
        self.list_view_1.setModel(self.listview_model_1)
    # popola la prima lista con la targa della barca

    def update_ui_2(self):
        self.listview_model_2 = QStandardItemModel(self.list_view_2)
        for posizione in self.controller.get_lista_posizioni():
            item = QStandardItem()
            item.setText("Lat: " + posizione.latitudine + "  Long: " + posizione.longitudine)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(12)
            item.setFont(font)
            self.listview_model_2.appendRow(item)
        self.list_view_2.setModel(self.listview_model_2)
    # popola la seconda lista con la posizione della barca
