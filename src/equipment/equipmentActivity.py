# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow
from src.equipment.equipmentUI import Ui_equipmentActivity
from src.equipment.equipmentToDB import equipmentToDB
from libs.MySQLdb import MySQLdb
from src.dialog.dialogActivity import dialogActivity

class equipmentActivity(QMainWindow, equipmentToDB):
    def __init__(self, credentials, parent=None):
        self.credentials=credentials
        super().__init__(parent)
        self.ui = Ui_equipmentActivity()
        self.ui.setupUi(self)
        self.show()
        self.ui.brandComboBox.addItems(self.brands)
        self.ui.brandComboBox.currentIndexChanged.connect(self.loadMatchingModels)
        self.ui.modelComboBox.currentIndexChanged.connect(self.loadMatchingSerials)
        self.ui.serialNumberComboBox.currentIndexChanged.connect(self.loadEquipment)

    def loadMatchingModels(self):
        brand=self.brands[self.ui.brandComboBox.currentIndex()]
        self.ui.modelComboBox.setEnabled(brand!="Sin escoger")
        self.ui.serialNumberComboBox.setEnabled(False)
        self.ui.modelComboBox.clear()
        self.ui.serialNumberComboBox.clear()
        if brand!="Sin escoger":
            self.models=self.getModels(brand)
            self.ui.modelComboBox.addItems(self.models)
    
    def loadMatchingSerials(self):
        brand=self.brands[self.ui.brandComboBox.currentIndex()]
        model=self.models[self.ui.modelComboBox.currentIndex()]
        self.ui.serialNumberComboBox.clear()
        if model!="Sin escoger" and model!="":
            self.ui.serialNumberComboBox.setEnabled(True)
            self.serialNumbers=self.getSerials(brand, model)
            self.ui.serialNumberComboBox.addItems(self.serialNumbers)
        else:
            self.ui.serialNumberComboBox.setEnabled(False)

    def loadEquipment(self):
        brand=self.brands[self.ui.brandComboBox.currentIndex()]
        model=self.models[self.ui.modelComboBox.currentIndex()]
        serialNumber=self.serialNumbers[self.ui.serialNumberComboBox.currentIndex()]
        if model!="Sin escoger":
            self.ui.comment.setText(self.getComment(brand, model, serialNumber))