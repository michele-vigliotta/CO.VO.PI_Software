from PyQt5.QtWidgets import QApplication, QDialog
from home.views.VistaHome import VistaHome
import sys

from login import Login


if __name__ == '__main__':

    app = QApplication(sys.argv)
    login = Login()

    # se il login ha successo, visualizza la vista home
    if login.exec_() == QDialog.Accepted:
            vista_home = VistaHome()
            vista_home.show()
            sys.exit(app.exec_())


