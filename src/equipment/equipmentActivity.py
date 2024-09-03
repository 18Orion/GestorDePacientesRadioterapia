# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow
from src.equipment.equipmentUI import Ui_equipmentActivity
from src.equipment.equipmentToDB import equipmentToDB
from libs.MySQLdb import MySQLdb
from src.dialog.dialogActivity import dialogActivity
from libs.globalVars import MANTAINEMENT_TYPE

class equipmentActivity(QMainWindow, equipmentToDB):
    def __init__(self, credentials, parent=None):
        self.credentials=credentials
        super().__init__(parent)
        self.ui = Ui_equipmentActivity()
        self.ui.setupUi(self)
        self.operations=[]
        self.show()
        self.ui.brandComboBox.addItems(self.brands)
        self.ui.technicianComboBox.addItems(self.technicians)
        self.ui.radiophysicianComboBox.addItems(self.radiophysicist)
        self.ui.typeOfOperation.addItems(MANTAINEMENT_TYPE)
        self.ui.brandComboBox.currentIndexChanged.connect(self.loadMatchingModels)
        self.ui.modelComboBox.currentIndexChanged.connect(self.loadMatchingSerials)
        self.ui.serialNumberComboBox.currentIndexChanged.connect(self.loadEquipment)
        self.ui.save.clicked.connect(self.writeSQL)


    def loadMatchingModels(self):
        self.deviceChosen(False)
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
            self.deviceChosen(False)
            self.ui.serialNumberComboBox.setEnabled(True)
            self.serialNumbers=self.getSerials(brand, model)
            self.ui.serialNumberComboBox.addItems(self.serialNumbers)
        else:
            self.ui.serialNumberComboBox.setEnabled(False)

    def loadEquipment(self):
        self.deviceChosen(True)
        brand=self.brands[self.ui.brandComboBox.currentIndex()]
        model=self.models[self.ui.modelComboBox.currentIndex()]
        serialNumber=self.serialNumbers[self.ui.serialNumberComboBox.currentIndex()]
        if model!="Sin escoger":
            self.ui.comment.setText(self.getComment(brand, model, serialNumber))
            self.deviceChosen(True)

    def deviceChosen(self, chosen):
        self.ui.operation.setEnabled(chosen)
        self.ui.data.setEnabled(chosen)
        self.ui.save.setEnabled(chosen)
        self.operations.clear()
        self.ui.operation.clear()
        if chosen:
            self.operations=self.getMatchingOperations(self.serialNumbers[self.ui.serialNumberComboBox.currentIndex()])
            self.ui.operation.addItem("Nueva operación")
            self.ui.operation.addItems(range(1, len(self.operations)+1))
        else:
            self.ui.historyTable.setRowCount(0)

    def loadOperationsTable(self):
        for i in self.operations:
            for a in range(1, len(i)):
                pass

    def writeSQL(self):
        self.sql.saveMantainement((self.serialNumbers[self.ui.serialNumberComboBox.currentIndex()],
            self.ui.typeOfOperation.currentIndex(),
            self.radiophysicist[self.ui.radiophysicianComboBox.currentIndex()],
            self.technicians[self.ui.technicianComboBox.currentIndex()],
            self.ui.beginDate.date().toPython(),
            self.ui.endDate.date().toPython()))