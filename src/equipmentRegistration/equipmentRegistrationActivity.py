# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow
from src.equipmentRegistration.equipmentRegistrationUI import Ui_equipmentRegistrationActivity
from libs.MySQLdb import MySQLdb
from src.dialog.dialogActivity import dialogActivity

class equipmentRegistrationActivity(QMainWindow):
    #An activity to registrate equipment
    def __init__(self, credentials, parent=None):
        super().__init__(parent)
        self.ui = Ui_equipmentRegistrationActivity()
        self.ui.setupUi(self)
        self.ui.centreEdit.setFocus()        #Set focus
        self.sql=MySQLdb(credentials)
        self.sql.connectToEquipmentDB()
        #Slot definition
        self.ui.registrateEquipment.clicked.connect(self.registrateEquipment)


    def registrateEquipment(self):
        if self.placementModelFilled() and self.modelInfoFilled() and self.generatorInfoFilled():
            equipment=(self.ui.centreEdit.text(),
                self.ui.serviceEdit.text(),
                self.ui.locationEdit.text(),
                self.ui.brandEdit.text(),
                self.ui.modelEdit.text(),
                self.ui.serialNumberEdit.text(),
                self.ui.generatorBrandEdit.text(),
                self.ui.generatorModelEdit.text(),
                self.ui.generatorSerialNumberEdit.text())
            self.sql.saveEquipment(equipment)
        else:
            self.dialog=dialogActivity("Rellene todos los campos")
            
    def placementModelFilled(self):
        return self.ui.centreEdit.text() and self.ui.serviceEdit.text() and self.ui.locationEdit.text()
    
    def modelInfoFilled(self):
        return self.ui.brandEdit.text() and self.ui.modelEdit.text() and self.ui.serialNumberEdit.text()

    def generatorInfoFilled(self):
        return self.ui.generatorBrandEdit.text() and self.ui.generatorModelEdit.text() and self.ui.generatorSerialNumberEdit.text()
