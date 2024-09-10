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
        self.comboBoxList=(self.ui.centreComboBox,
            self.ui.serviceComboBox,
            self.ui.locationComboBox,
            self.ui.brandComboBox,
            self.ui.modelComboBox,
            self.ui.serialComboBox)
        #Populates the widgets
        self.ui.centreComboBox.addItems(self.getAllPosibilities(0, self.sql.equipmentTable))
        self.ui.technicianComboBox.addItems(self.technicians)
        self.ui.radiophysicianComboBox.addItems(self.radiophysicist)
        self.ui.typeOfOperation.addItems(MANTAINEMENT_TYPE)
        self.ui.beginDate.setDate(date.today())
        self.ui.endDate.setDate(date.today())
        #Slot definition
        self.ui.save.clicked.connect(self.writeSQL)
        self.ui.centreComboBox.currentIndexChanged.connect(lambda: self.loadNext(self.ui.centreComboBox))
        self.ui.serviceComboBox.currentIndexChanged.connect(lambda: self.loadNext( self.ui.serviceComboBox))
        self.ui.locationComboBox.currentIndexChanged.connect(lambda: self.loadNext(self.ui.locationComboBox))
        self.ui.brandComboBox.currentIndexChanged.connect(lambda: self.loadNext(self.ui.brandComboBox))
        self.ui.modelComboBox.currentIndexChanged.connect(lambda: self.loadNext(self.ui.modelComboBox))
        self.ui.serialComboBox.currentIndexChanged.connect(self.loadSerialNumber)
        self.ui.operation.currentIndexChanged.connect(self.onOperationChanged)

    def onOperationChanged(self):
        if self.ui.operation.currentText()!="Nueva operación" and self.ui.operation.currentText():
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

    
    def writeSQL(self):
        if self.ui.operation.currentIndex()==0:
            self.operationNumber=len(self.operations)+1
            overwrite=False
        else:
            self.operationNumber=int(self.ui.operation.currentText())
            overwrite=True
        self.sql.saveMantainement((self.ui.serialComboBox.currentText(),
            self.operationNumber,
            self.ui.typeOfOperation.currentIndex(),
            self.ui.radiophysicianComboBox.currentText(),
            self.ui.technicianComboBox.currentText(),
            self.ui.beginDate.date().toPython(),
            self.ui.endDate.date().toPython()), overwrite)
        self.sql.loadMantainementTable()
        self.deviceChosen(True)
        self.ui.operation.setCurrentIndex(self.operationNumber)

    def loadNext(self, comboBox):
        currentComboBoxIndex=self.comboBoxList.index(comboBox)
        for i in range(currentComboBoxIndex+1, len(self.comboBoxList)):
            self.comboBoxList[i].clear()                #Clears the content of every combobox
            self.comboBoxList[i].setEnabled(False)      #Disables every combobox
        if comboBox.currentText()!="Sin escoger" and comboBox.currentText():
            self.setParam(comboBox.currentText(), currentComboBoxIndex)
            search=self.searchBy()
            next(search)
            self.comboBoxList[currentComboBoxIndex+1].setEnabled(True)
            self.comboBoxList[currentComboBoxIndex+1].addItems(next(search))
        
    def loadSerialNumber(self):
        self.operations=self.getMatchingOperations(self.ui.serialComboBox.currentText())
        self.deviceChosen(self.ui.serialComboBox.currentText()!="Sin escoger" and self.ui.serialComboBox.currentText()!="")

    def deviceChosen(self, chosen):
        self.ui.operation.setEnabled(chosen)
        self.ui.data.setEnabled(chosen)
        self.ui.save.setEnabled(chosen)
        self.operations.clear()
        self.ui.operation.clear()
        if chosen:
            self.operations=self.getMatchingOperations(self.ui.serialComboBox.currentText())
            self.ui.operation.addItem("Nueva operación")
            for i in range(1, len(self.operations)+1):
                self.ui.operation.addItem(str(i))
            self.loadOperationsTable()
        else:
            self.ui.historyTable.setRowCount(0)

    def loadOperationsTable(self):
        self.ui.historyTable.setRowCount(0)
        for rowNumber in range(len(self.operations)):
            i=self.operations[rowNumber]
            self.ui.historyTable.insertRow(rowNumber)
            self.ui.historyTable.setItem(rowNumber, 0, QTableWidgetItem(str(i[1])))
            self.ui.historyTable.setItem(rowNumber, 1, QTableWidgetItem(str(MANTAINEMENT_TYPE[i[2]])))
            self.ui.historyTable.setItem(rowNumber, 2, QTableWidgetItem(str(i[3])))
            self.ui.historyTable.setItem(rowNumber, 3, QTableWidgetItem(str(i[4])))
            self.ui.historyTable.setItem(rowNumber, 4, QTableWidgetItem(str(toSpanishDate(i[5]))))
            self.ui.historyTable.setItem(rowNumber, 5, QTableWidgetItem(str(toSpanishDate(i[6]))))