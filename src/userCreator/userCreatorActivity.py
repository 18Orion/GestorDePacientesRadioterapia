# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from src.dialog.dialogActivity import dialogActivity
from libs.MySQLdb import MySQLdb
from .userCreatorUI import Ui_userCreatorActivity

class userCreatorActivity(QMainWindow):
    def __init__(self, credentials, parent=None):
        self.sql=MySQLdb(credentials)
        super().__init__(parent)
        self.ui = Ui_userCreatorActivity()
        self.ui.setupUi(self)
        self.ui.createUser.clicked.connect(self.createSQLUser)
    
    def createSQLUser(self):
        user=self.ui.user.text()
        passwd=self.ui.password.text()
        passwdRepeat=self.ui.repeatPassword.text()
        if (user.isalnum())and(user):
            if (passwd):
                if(passwd==passwdRepeat):
                    try:
                        self.sql.createUser(user, passwd)
                        self.dialog=dialogActivity("Usuario creado")
                    except:
                        self.dialog=dialogActivity("Error al crear usuario")
                else:
                    self.dialog=dialogActivity("Las contraseñas no coinciden.")
            else:
                self.dialog=dialogActivity("La contraseña está vacía.")
        else:
            self.dialog=dialogActivity("El usuario contiene errores. Por favor reviselo.")
