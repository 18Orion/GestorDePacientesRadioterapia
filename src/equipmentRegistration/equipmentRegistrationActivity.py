# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow
from src.equipmentRegistration.equipmentRegistrationUI import Ui_equipmentRegistrationActivity
from libs.MySQLdb import MySQLdb
from src.dialog.dialogActivity import dialogActivity

class equipmentRegistrationActivity(QMainWindow):
    def __init__(self, credentials, parent=None):
        super().__init__(parent)
        self.ui = Ui_equipmentRegistrationActivity()
        self.ui.setupUi(self)
        self.show()
        self.ui.registrateEquipment.clicked.connect(self.registrateEquipment)
        self.sql=MySQLdb(credentials)
        self.sql.connectToEquipmentDB()
    
    def registrateEquipment(self):
        brand=self.ui.brandEdit.text()
        model=self.ui.modelEdit.text()
        serialNumber=self.ui.serialNumberEdit.text()
        comment=self.ui.commentEdit.text()
        if (brand)and(model)and(serialNumber):
            try:
                self.sql.saveEquipment((brand, model, serialNumber, comment))
                self.dialog=dialogActivity("Equipamiento registrado")
            except Exception as err:
                self.dialgo=dialogActivity("Error: "+str(err)+" al registrar el equipo")
        else:
            self.dialgo=dialogActivity("Rellene marca, modelo y número de serie")

