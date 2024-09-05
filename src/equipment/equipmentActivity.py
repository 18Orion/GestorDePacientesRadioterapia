# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QTableWidgetItem
from src.equipment.equipmentUI import Ui_equipmentActivity
from src.equipment.equipmentToDB import equipmentToDB
from libs.MySQLdb import MySQLdb
from src.dialog.dialogActivity import dialogActivity
from libs.globalVars import MANTAINEMENT_TYPE
from libs.funcs import toSpanishDate
from datetime import date

class equipmentActivity(QMainWindow, equipmentToDB):
    def __init__(self, credentials, parent=None):
        self.credentials=credentials
        super().__init__(parent)
        self.ui = Ui_equipmentActivity()
        self.ui.setupUi(self)
        self.operations=[]
        self.show()
        #Populates the widgets
        self.ui.brandComboBox.addItems(self.brands)
        self.ui.technicianComboBox.addItems(self.technicians)
        self.ui.radiophysicianComboBox.addItems(self.radiophysicist)
        self.ui.typeOfOperation.addItems(MANTAINEMENT_TYPE)
        self.ui.beginDate.setDate(date.today())
        self.ui.endDate.setDate(date.today())
        #Slot definition
        self.ui.brandComboBox.currentIndexChanged.connect(self.loadMatchingModels)
        self.ui.modelComboBox.currentIndexChanged.connect(self.loadMatchingSerials)
        self.ui.serialNumberComboBox.currentIndexChanged.connect(self.loadEquipment)
        self.ui.save.clicked.connect(self.writeSQL)
        self.ui.operation.currentIndexChanged.connect(self.onOperationChanged)


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
        self.deviceChosen(False)
        if model!="Sin escoger" and model!="":
            self.ui.serialNumberComboBox.setEnabled(True)
            self.serialNumbers=self.getSerials(brand, model)
            self.ui.serialNumberComboBox.addItems(self.serialNumbers)
        else:
            self.ui.serialNumberComboBox.setEnabled(False)

    def loadEquipment(self):
        self.deviceChosen(False)
        brand=self.brands[self.ui.brandComboBox.currentIndex()]
        model=self.models[self.ui.modelComboBox.currentIndex()]
        serialNumber=self.serialNumbers[self.ui.serialNumberComboBox.currentIndex()]
        if serialNumber!="Sin escoger":
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
            for i in range(1, len(self.operations)+1):
                self.ui.operation.addItems(str(i))
            self.loadOperationsTable()
        else:
            self.ui.historyTable.setRowCount(0)

    def loadOperationsTable(self):
        self.ui.historyTable.setRowCount(0)
        for rowNumber in range(len(self.operations)):
            i=self.operations[rowNumber]
            self.ui.historyTable.insertRow(rowNumber)
            #Writes the tuple
            self.ui.historyTable.setItem(rowNumber, 0, QTableWidgetItem(str(i[1])))
            self.ui.historyTable.setItem(rowNumber, 1, QTableWidgetItem(str(MANTAINEMENT_TYPE[i[2]])))
            self.ui.historyTable.setItem(rowNumber, 2, QTableWidgetItem(str(i[3])))
            self.ui.historyTable.setItem(rowNumber, 3, QTableWidgetItem(str(i[4])))
            self.ui.historyTable.setItem(rowNumber, 4, QTableWidgetItem(str(toSpanishDate(i[5]))))
            self.ui.historyTable.setItem(rowNumber, 5, QTableWidgetItem(str(toSpanishDate(i[6]))))


    def writeSQL(self):
        if self.ui.operation.currentIndex()==0:         #Gives the operation a new number
            self.operationNumber=len(self.operations)+1
        else:
            self.operationNumber=self.ui.operation.currentIndex()   #Gives the operation its number
        self.sql.saveMantainement((self.serialNumbers[self.ui.serialNumberComboBox.currentIndex()],
            self.operationNumber,
            self.ui.typeOfOperation.currentIndex(),
            self.radiophysicist[self.ui.radiophysicianComboBox.currentIndex()],
            self.technicians[self.ui.technicianComboBox.currentIndex()],
            self.ui.beginDate.date().toPython(),
            self.ui.endDate.date().toPython()), self.ui.operation.currentIndex()!=0)
        self.sql.loadMantainementTable()                        #Reloads the sql
        self.deviceChosen(True)
        self.ui.operation.setCurrentIndex(self.operationNumber) #Changes the operation number to the newly given number

    def onOperationChanged(self):
        if self.ui.operation.currentIndex()!=0:
            #If the operation exists it loads it
            self.operationNumber=self.ui.operation.currentIndex()-1
            loadOp=self.operations[self.ui.operation.currentIndex()-1]
            self.ui.typeOfOperation.setCurrentIndex(loadOp[2])
            self.ui.radiophysicianComboBox.setCurrentIndex(self.radiophysicist.index(loadOp[3]))
            self.ui.technicianComboBox.setCurrentIndex(self.technicians.index(loadOp[4]))
            self.ui.beginDate.setDate(loadOp[5])
            self.ui.endDate.setDate(loadOp[6])
        else:
            #If the operation is new it clears all fields
            self.ui.typeOfOperation.setCurrentIndex(0)
            self.ui.radiophysicianComboBox.setCurrentIndex(0)
            self.ui.technicianComboBox.setCurrentIndex(0)
            self.ui.beginDate.setDate(date.today())
            self.ui.endDate.setDate(date.today())
        