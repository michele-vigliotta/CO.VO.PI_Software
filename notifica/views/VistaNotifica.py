from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QMessageBox
from notifica.controller.ControlloreNotifica import ControlloreNotifica


class VistaNotifica(QWidget):
    def __init__(self, messaggio):
        super(VistaNotifica, self).__init__()

        self.messaggio = messaggio

        self.controller = ControlloreNotifica()

        self.setWindowTitle("Notifica")

        label = QLabel("Barche & Quote")
        label.setStyleSheet('color:#000dc3')
        font_label = label.font()
        font_label.setPointSize(12)
        label.setFont(font_label)

        self.text = QTextEdit()
        self.text.setReadOnly(True)
        font = self.text.font()
        font.setPointSize(11)
        self.text.setFont(font)
        self.text.setStyleSheet("background-color:white")
        self.text.setText(self.messaggio)

        invia_button = QPushButton("Invia")
        invia_button.clicked.connect(self.invia_messaggio)
        invia_button.setIcon(QIcon('icone/notifica'))
        invia_button.setIconSize(QSize(30, 30))
        invia_button.setStyleSheet('background-color:white;color:#ff8000')
        font_invia_button = invia_button.font()
        font_invia_button.setPointSize(12)
        invia_button.setFont(font_invia_button)

        v_layout = QVBoxLayout()
        v_layout.addWidget(label)
        v_layout.addWidget(self.text)
        v_layout.addWidget(invia_button)

        self.setLayout(v_layout)
        self.setStyleSheet('background-color:lightblue')
        self.setWindowIcon(QIcon('icone/notifica.png'))

    def invia_messaggio(self):
        self.controller.invia_messaggio(self.messaggio)


