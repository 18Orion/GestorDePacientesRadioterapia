from .loginUI import Ui_login
from PySide6.QtWidgets import QApplication, QMainWindow
import mysql.connector
from src.dialog.dialogActivity import dialogActivity
from src.launcher.launcherActivity import launcherActivity


class loginActivity(QMainWindow):
    def __init__(self, parent=None):
        global logIn
        super().__init__(parent)
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.ui.logIn.clicked.connect(self.loginClicked)
        self.ui.user.returnPressed.connect(self.moveOnToPassword)
        self.ui.password.returnPressed.connect(self.loginClicked)
        logIn=self

    def loginClicked(self):
        try:
            DB=mysql.connector.connect(host='192.168.1.141',
                user=self.ui.user.text(),
                password=self.ui.password.text())
            self.launcher=launcherActivity(credentials=(self.ui.user.text(),self.ui.password.text()))
            self.launcher.show()
            self.hide()
        except mysql.connector.errors.ProgrammingError:
            self.ui.password.setText("")
            self.dialog=dialogActivity("Usuario o contraseña incorrecta.")
        except Exception as err:
            self.dialog=dialogActivity("Fallo inesperado: "+str(err))
    
    def moveOnToPassword(self):
        self.ui.password.setFocus()