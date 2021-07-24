from PyQt5.QtWidgets import QDialog, QLabel, QGridLayout, QListView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from supervisione.entrate_uscite.controller.ControlloreEntrateUscite import ControlloreEntrateUscite


class VistaEntrateUscite(QDialog):
    def __init__(self):
        super(VistaEntrateUscite, self).__init__()

        self.controller = ControlloreEntrateUscite()

        grid_layout = QGridLayout()

        self.label_1 = QLabel("Imbarcazioni")
        self.label_1.setStyleSheet('color:#000dc3')
        font_label = self.label_1.font()
        font_label.setPointSize(14)
        self.label_1.setFont(font_label)
        self.label_2 = QLabel("   Uscita")
        self.label_2.setStyleSheet('color:#000dc3')
        font_label = self.label_2.font()
        font_label.setPointSize(14)
        self.label_2.setFont(font_label)
        self.label_3 = QLabel("Ingresso")
        self.label_3.setStyleSheet('color:#000dc3')
        font_label = self.label_3.font()
        font_label.setPointSize(14)
        self.label_3.setFont(font_label)

        self.list_view_1 = QListView()
        self.list_view_1.setStyleSheet("Background-color: white")
        self.list_view_2 = QListView()
        self.list_view_2.setStyleSheet("Background-color: white")
        self.list_view_3 = QListView()
        self.list_view_3.setStyleSheet("Background-color: white")

        self.update_ui_1()
        self.update_ui_2()
        self.update_ui_3()

        grid_layout.addWidget(self.label_1, 0, 0)
        grid_layout.addWidget(self.label_2, 0, 1)
        grid_layout.addWidget(self.label_3, 0, 2)
        grid_layout.addWidget(self.list_view_1, 1, 0)
        grid_layout.addWidget(self.list_view_2, 1, 1)
        grid_layout.addWidget(self.list_view_3, 1, 2)

        self.setLayout(grid_layout)
        self.resize(400, 400)
        self.setStyleSheet("Background-color: lightblue")
        self.setWindowTitle("Lista entrate e uscite")
        self.setContentsMargins(10, 10, 10, 10)
        self.setWindowIcon(QIcon("icone/icona_entrate_uscite.png"))

    def update_ui_1(self):
        self.listview_model_1 = QStandardItemModel(self.list_view_1)
        for entrata_uscita in self.controller.get_lista_entrate_uscite():
            item = QStandardItem()
            item.setText(entrata_uscita.targa)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(12)
            item.setFont(font)
            self.listview_model_1.appendRow(item)
        self.list_view_1.setModel(self.listview_model_1)
    # popola la prima lista con le targhe delle barche

    def update_ui_2(self):
        self.listview_model_2 = QStandardItemModel(self.list_view_2)
        for entrata_uscita in self.controller.get_lista_entrate_uscite():
            item = QStandardItem()
            item.setText(entrata_uscita.uscita)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(12)
            item.setFont(font)
            self.listview_model_2.appendRow(item)
        self.list_view_2.setModel(self.listview_model_2)
    # popola la seconda lista con l'orario d'uscita delle barche

    def update_ui_3(self):
        self.listview_model_3 = QStandardItemModel(self.list_view_3)
        for entrata_uscita in self.controller.get_lista_entrate_uscite():
            item = QStandardItem()
            item.setText(entrata_uscita.ingresso)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(12)
            item.setFont(font)
            self.listview_model_3.appendRow(item)
        self.list_view_3.setModel(self.listview_model_3)
    # popola la terza lista con l'orario d'ingresso delle barche
