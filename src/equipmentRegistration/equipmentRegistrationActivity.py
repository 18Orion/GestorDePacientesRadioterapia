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
        self.ui.brandEdit.setFocus()        #Set focus
        self.sql=MySQLdb(credentials)
        self.sql.connectToEquipmentDB()
        #Slot definition
        self.ui.registrateEquipment.clicked.connect(self.registrateEquipment)
        self.ui.brandEdit.returnPressed.connect(self.ui.modelEdit.setFocus)
        self.ui.modelEdit.returnPressed.connect(self.ui.serialNumberEdit.setFocus)
        self.ui.serialNumberEdit.returnPressed.connect(self.ui.commentEdit.setFocus)
    
    def registrateEquipment(self):
        brand=self.ui.brandEdit.text()
        model=self.ui.modelEdit.text()
        serialNumber=self.ui.serialNumberEdit.text()
        comment=self.ui.commentEdit.text()
        if (brand)and(model)and(serialNumber):      #If all the important gaps are filled the equipment is registrated
            try:
                self.sql.saveEquipment((brand, model, serialNumber, comment))
                self.dialog=dialogActivity("Equipamiento registrado")
            except Exception as err:
                self.dialgo=dialogActivity("Error: "+str(err)+" al registrar el equipo")
        else:
            self.dialgo=dialogActivity("Rellene marca, modelo y número de serie")

