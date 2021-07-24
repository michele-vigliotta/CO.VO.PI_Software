from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QTextEdit

from barca.controller.ControlloreBarca import ControlloreBarca


class VistaBarca(QWidget):
    def __init__(self, barca, elimina_barca, elimina_callback, parent=None):
        super(VistaBarca, self).__init__(parent)
        self.controller = ControlloreBarca(barca)
        self.elimina_barca = elimina_barca
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        label_info_barca = QLabel("Info Barca ")
        label_info_barca.setStyleSheet('color:#000dc3')
        font_label = label_info_barca.font()
        font_label.setPointSize(12)
        label_info_barca.setFont(font_label)
        v_layout.addWidget(label_info_barca)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        text = QTextEdit()
        text.setReadOnly(True)
        font = text.font()
        font.setPointSize(11)
        text.setFont(font)
        text.setStyleSheet("background-color:white")
        text.setText(self.get_testo_da_mostrare())
        v_layout.addWidget(text)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        font_btn_elimina = btn_elimina.font()
        font_btn_elimina.setPointSize(12)
        btn_elimina.setFont(font_btn_elimina)
        btn_elimina.setStyleSheet('background-color:white;color:#ff8000')
        btn_elimina.clicked.connect(self.elimina_barca_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_barca())
        self.setStyleSheet('background-color:lightblue')
        self.setWindowIcon(QIcon('icone/gestionebarche.png'))

    # metodo che ritorna il testo da mostrare nel QTextEdit
    def get_testo_da_mostrare(self):
        testo = " Targa: {}".format(self.controller.get_targa_barca()) + \
                "\n Nome Referente: {}".format(self.controller.get_nomereferente_barca()) + \
                "\n Cognome Referente: {}".format(self.controller.get_cognomereferente_barca()) + \
                "\n Codice Fiscale: {}".format(self.controller.get_cf_barca()) + \
                "\n Telefono: {}".format(self.controller.get_telefono_barca()) + \
                "\n Equipaggio: {}".format(self.controller.get_equipaggio_barca()) + \
                "\n Licenza: {}".format(self.controller.get_licenza_barca())
        return testo

    def elimina_barca_click(self):
        self.elimina_barca(self.controller.get_targa_barca())
        self.elimina_callback()
        self.close()
