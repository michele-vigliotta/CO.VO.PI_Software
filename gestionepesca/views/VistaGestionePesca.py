from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIntValidator, QIcon, QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QSpacerItem, QSizePolicy, QMessageBox
from notifica.views.VistaNotifica import VistaNotifica
from gestionepesca.controller.ControlloreGestionePesca import ControlloreGestionePesca


class VistaGestionePesca(QWidget):

    def __init__(self, parent=None):
        super(VistaGestionePesca, self).__init__(parent)

        self.controller = ControlloreGestionePesca()

        v_layout = QVBoxLayout()

        label_inserisci_quota = QLabel("Inserisci Quota Totale: ")
        label_inserisci_quota.setStyleSheet('color:#000dc3')
        font_label = label_inserisci_quota.font()
        font_label.setPointSize(12)
        label_inserisci_quota.setFont(font_label)

        self.line_edit = QLineEdit()
        self.is_only_int = QIntValidator()
        self.line_edit.setValidator(self.is_only_int)
        self.line_edit.setStyleSheet('background-color:white')
        font_line_edit = self.line_edit.font()
        font_line_edit.setPointSize(12)
        self.line_edit.setFont(font_line_edit)

        v_layout.addWidget(label_inserisci_quota)
        v_layout.addWidget(self.line_edit)
        v_layout.addWidget(self.get_generic_button("Conferma", self.save_messaggio, "icone/conferma.png"))

        self.bollino = QLabel()
        v_layout.addWidget(self.bollino)
        label_trasp = QLabel()
        v_layout.addWidget(label_trasp)

        v_layout.addWidget(self.get_generic_button("Notifica", self.go_notifica, "icone/notifica.png"))

        v_layout.addStretch()

        self.setLayout(v_layout)

        self.setWindowTitle("Gestione Pesca")
        self.setStyleSheet('background-color:lightblue')
        self.setWindowIcon(QIcon('icone/gestionepesca.png'))
        self.setFixedWidth(280)
        self.setFixedHeight(200)

    def get_generic_button(self, titolo, on_click, icona):
        button = QPushButton(titolo)
        button.setFont(QFont('Times', 12))
        button.setStyleSheet('background-color:white;color:#ff8000')
        button.setIcon(QIcon(icona))
        button.setIconSize(QSize(30, 30))
        button.clicked.connect(on_click)
        return button

    '''metodo che effettua un duplice controllo. 
        se la quota totale è > di 200 viene settatto un bollino verde(in caso contrario rosso) 
        e vengono calcolate le quote parziali, che inserite in un testo verrano poi inviate tramite notifica'''

    def save_messaggio(self):

        if self.line_edit.text() == "" :
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci la Quota Totale.',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        if int(self.line_edit.text()) < 200 :
            self.bollino.setPixmap(QPixmap('icone/bollinorosso.png'))
        else:

            self.bollino.setPixmap(QPixmap('icone/bollinoverde.png'))
            self.testo_tot = " "
            quota_tot = int(self.line_edit.text())
            barche_3 = self.controller.get_barche_3()
            z = int((quota_tot - (barche_3 * 2))/(self.controller.get_barche_tot()))
            x = z+2
            for barca in self.controller.get_lista_barche():
                if barca.equipaggio == "3":
                    self.testo_tot += " \n" + barca.nome + " - " + "quota : " + str(x)
                else:
                    self.testo_tot += " \n" + barca.nome + " - " + "quota : " + str(z)


    def go_notifica(self):

        if self.line_edit.text() == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci prima la Quota Totale.',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        if int(self.line_edit.text()) < 200 :
            QMessageBox.critical(self, 'Errore', 'Quota Giornaliera non sufficiente.',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        self.vista_notifica = VistaNotifica(self.testo_tot)
        self.vista_notifica.show()











