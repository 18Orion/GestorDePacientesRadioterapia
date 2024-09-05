import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from src.credentials.credentialsUI import Ui_Credentials
from libs.MySQLdb import MySQLdb
from time import sleep
from src.dialog.dialogActivity import dialogActivity

class credentialsActivity(QMainWindow):
    def __init__(self, credentials ,parent=None):
        super().__init__(parent)
        self.credentials=credentials
        self.sql=MySQLdb(credentials)
        self.ui = Ui_Credentials()
        self.ui.setupUi(self)
        self.ui.user.setText(credentials[0])
        self.ui.changePassword.clicked.connect(self.changePasswordClicked)

    def changePasswordClicked(self):
        #Changes the password if they coincide
        if (self.ui.confPassword.text()==self.ui.newPassword.text())and(self.ui.oldPassword.text()==self.credentials[1]):
            passwd=[self.ui.newPassword.text()]
            self.sql.changePassword(passwd)
            self.dialog=dialogActivity("Contraseña cambiada, cerrando aplicación...", exit)
        elif not(self.ui.confPassword.text()==self.ui.newPassword.text()):
            self.dialog=dialogActivity("Las contraseñas no coinciden.")
        else:
            self.dialog=dialogActivity("Contraseña actual incorrecta.")
        self.ui.confPassword.clear()
        self.ui.newPassword.clear()
        self.ui.oldPassword.clear()