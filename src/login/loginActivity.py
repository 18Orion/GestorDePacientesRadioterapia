from .loginUI import Ui_login
from PySide6.QtWidgets import QApplication, QMainWindow
import mysql.connector
from src.dialog.dialogActivity import dialogActivity
from src.launcher.launcherActivity import launcherActivity
from libs.confReader import confReader


class loginActivity(QMainWindow):
    def __init__(self, parent=None):
        self.conf=confReader()
        super().__init__(parent)
        self.ui = Ui_login()
        self.ui.setupUi(self)
        #Slot connect
        self.ui.logIn.clicked.connect(self.loginClicked)
        self.ui.user.returnPressed.connect(sself.ui.password.setFocus)
        self.ui.password.returnPressed.connect(self.loginClicked)

    def loginClicked(self):
        try:
            #Try connection with given credentials
            DB=mysql.connector.connect(host=self.conf.host,
                user=self.ui.user.text(),
                password=self.ui.password.text())
            #If connection is stablished launcher is created
            #If not, an exception is raised
            self.launcher=launcherActivity(credentials=(self.ui.user.text(),self.ui.password.text()))
            self.launcher.show()
            self.hide()
        except mysql.connector.errors.ProgrammingError:
            #User or password incorrect
            self.ui.password.setText("")
            self.dialog=dialogActivity("Usuario o contraseña incorrecta.")
        except Exception as err:
            #Show unhandled exception
            self.dialog=dialogActivity("Fallo inesperado: "+str(err))
    