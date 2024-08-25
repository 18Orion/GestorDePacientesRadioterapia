from .loginUI import Ui_login
from PySide6.QtWidgets import QApplication, QMainWindow
import mysql.connector
from src.dialog.dialogActivity import dialogActivity
from src.launcher.launcherActivity import launcherActivity

class loginActivity(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.ui.logIn.clicked.connect(self.loginClicked)
        self.ui.user.returnPressed.connect(self.moveOnToPassword)
        self.ui.password.returnPressed.connect(self.loginClicked)

    def loginClicked(self):
        DB=mysql.connector.connect(host='localhost',
            user=self.ui.user.text(),
            password=self.ui.password.text())
        self.launcher=launcherActivity(credentials=(self.ui.user.text(),self.ui.password.text()))
        self.launcher.show()
        self.hide()
        try:
            pass
        except:
            self.ui.password.setText("")
            self.dialog=dialogActivity("Usuario o contraseña incorrecta.")
    
    def moveOnToPassword(self):
        self.ui.password.setFocus()