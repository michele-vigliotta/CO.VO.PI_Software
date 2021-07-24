from PyQt5.QtWidgets import QDialog, QLabel, QGridLayout, QListView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from supervisione.violazioni.controller.ControlloreListaViolazioni import ControlloreListaViolazioni


class VistaListaViolazioni(QDialog):
    def __init__(self, parent=None):
        super(VistaListaViolazioni, self).__init__(parent)

        self.controller = ControlloreListaViolazioni()

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
        self.setWindowTitle("Lista violazioni")
        self.setStyleSheet("Background-color: lightblue")
        self.setContentsMargins(10, 10, 10, 10)
        self.setWindowIcon(QIcon('icone/icona_violazioni.png'))

    def update_ui_1(self):
        self.listview_model_1 = QStandardItemModel(self.list_view_1)
        for violazione in self.controller.get_lista_violazioni():
            item = QStandardItem()
            item.setText(violazione.targa)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(14)
            item.setFont(font)
            self.listview_model_1.appendRow(item)
        self.list_view_1.setModel(self.listview_model_1)
    # popola la prima lista con la targa della barca

    def update_ui_2(self):
        self.listview_model_2 = QStandardItemModel(self.list_view_2)
        for violazione in self.controller.get_lista_violazioni():
            item = QStandardItem()
            item.setText("Lat: " + violazione.latitudine + "     Long: " + violazione.longitudine)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(14)
            item.setFont(font)
            self.listview_model_2.appendRow(item)
        self.list_view_2.setModel(self.listview_model_2)
    # popola la seconda lista con la posizione della barca
