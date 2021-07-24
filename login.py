from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QSizePolicy, QSpacerItem


class Login(QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)

        self.setWindowTitle("CO.VO.PI Software")
        self.setStyleSheet('background-color:lightblue')

        self.setFixedWidth(223)
        self.setFixedHeight(400)

        self.icona = QLabel()
        self.icona.setPixmap(QPixmap('icone\login.png'))

        self.label_user = QLabel('Inserisci il nome utente:')
        self.label_user.setStyleSheet('color:#000dc3')
        font_label_user = self.label_user.font()
        font_label_user.setPointSize(12)
        self.label_user.setFont(font_label_user)

        self.text_user = QLineEdit() # spazio di riempimento per username
        self.text_user.setStyleSheet('background-color:white')
        font_user = self.text_user.font()
        font_user.setPointSize(11)
        self.text_user.setFont(font_user)

        self.layout_user = QVBoxLayout()
        self.layout_user.addWidget(self.label_user)
        self.layout_user.addWidget(self.text_user)

        self.label_password = QLabel('Inserisci la password: ')
        self.label_password.setStyleSheet('color:#000dc3')
        font_label_password = self.label_user.font()
        font_label_password.setPointSize(12)
        self.label_password.setFont(font_label_password)

        self.text_password = QLineEdit()  # spazio di riempimento per password
        self.text_password.setStyleSheet('background-color:white')
        font_password = self.text_password.font()
        font_password.setPointSize(11)
        self.text_password.setFont(font_password)

        self.text_password.setEchoMode(QLineEdit.Password)

        self.layout_password = QVBoxLayout()
        self.layout_password.addWidget(self.label_password)
        self.layout_password.addWidget(self.text_password)

        self.button_login = QPushButton('Login', self)
        self.button_login.setStyleSheet('background-color:white ; color:#ff8000')
        button_login_font = self.button_login.font()
        button_login_font.setPointSize(12)
        self.button_login.setFont(button_login_font)

        self.button_login.clicked.connect(self.gestione_login)

        layout = QVBoxLayout()

        layout.addWidget(self.icona)
        layout.addLayout(self.layout_user)

        layout.addLayout(self.layout_password)

        layout.addItem(QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        layout.addWidget(self.button_login)
        self.setLayout(layout)
        self.setWindowIcon(QIcon('icone\iconasoftware.png'))

    # metodo che controlla la correttezza dell'username e della password
    def gestione_login(self):
        if (self.text_user.text() == 'admin' and #USERNAME
                self.text_password.text() == 'password'): #PASSWORD
            self.accept()
        else:
            QMessageBox.warning(None,'Errore', 'Nome utente o password errata')


