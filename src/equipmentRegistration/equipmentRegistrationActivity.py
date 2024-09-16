# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow
from src.equipmentRegistration.equipmentRegistrationUI import Ui_equipmentRegistrationActivity
from libs.MySQLdb import MySQLdb
from src.dialog.dialogActivity import dialogActivity
from libs.confReader import confReader
from libs.funcs import getNameListFromFile

class equipmentRegistrationActivity(QMainWindow):
    #An activity to registrate equipment
    def __init__(self, credentials, parent=None):
        super().__init__(parent)
        conf=confReader()
        self.ui = Ui_equipmentRegistrationActivity()
        self.ui.setupUi(self)
        self.sql=MySQLdb(credentials)
        self.sql.connectToEquipmentDB()
        self.ui.centreComboBox.addItems(getNameListFromFile(conf.centreFile, 
            "#En este archivo figuran los centros con instalaciones radiactivas"))
        self.ui.serviceComboBox.addItems(getNameListFromFile(conf.serviceFile, 
            "#En este archivo figuran los servicios"))
        self.ui.brandComboBox.addItems(getNameListFromFile(conf.brandsFile,
            "#En este archivo se definen las marcas"))
        self.ui.generatorBrandComboBox.addItems(getNameListFromFile(conf.brandsFile,
            "#En este archivo se definen las marcas"))
        #Slot definition
        self.ui.registrateEquipment.clicked.connect(self.registrateEquipment)


    def registrateEquipment(self):
        if self.placementModelFilled() and self.modelInfoFilled() and self.generatorInfoFilled():
            equipment=(self.ui.centreComboBox.currentText(),
                self.ui.serviceComboBox.currentText(),
                self.ui.locationEdit.text(),
                self.ui.brandComboBox.currentText(),
                self.ui.modelLineEdit.text(),
                self.ui.serialNumberEdit.text(),
                self.ui.generatorBrandComboBox.currentText(),
                self.ui.generatorModelLineEdit.text(),
                self.ui.generatorSerialNumberEdit.text())
            self.sql.saveEquipment(equipment)
            self.dialog=dialogActivity("Equipo guardado")
        else:
            self.dialog=dialogActivity("Rellene todos los campos")
            
    def placementModelFilled(self):
        return self.isChosen(self.ui.centreComboBox.currentText()) and self.isChosen(self.ui.serviceComboBox.currentText()) and self.ui.locationEdit.text()
    
    def modelInfoFilled(self):
        return self.isChosen(self.ui.brandComboBox.currentText()) and self.ui.modelLineEdit.text() and self.ui.serialNumberEdit.text()

    def generatorInfoFilled(self):
        return self.isChosen(self.ui.generatorBrandComboBox.currentText()) and self.ui.generatorModelLineEdit.text() and self.ui.generatorSerialNumberEdit.text()

    def isChosen(self, option):
        return option!="Sin escoger"