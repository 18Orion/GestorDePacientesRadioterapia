from .dataToSQL import dataToSQL
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from .patientUI import Ui_MainWindow
from datetime import date
from libs.funcs import toSpanishDate, toOrdinal, isValidNUSHA
from src.dialog.dialogActivity import dialogActivity

"""
This class contains all methods used when buttons are clicked in main window.
It inherits from the class dataToSQL.py
"""

class patientActivity(QMainWindow, dataToSQL):
    def __init__(self, credentials,parent=None):
        self.credentials=credentials
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.autofillEventDate()        #Set current date to today

        #Populate combo boxes
        self.ui.treatmentOptions.addItems(self.TREATMENT_OPTIONS)     #added list to treatment options comboBox 
        self.ui.genderComboBox.addItems(self.GENDER_OPTIONS)
        self.ui.technicianComboBox.addItems(self.techniciansList)
        self.ui.dateType.addItems(self.DATE_OPTIONS)
        self.ui.doctorComboBox.addItems(self.doctorsList)
        self.ui.treatmentNumber.addItem("Nuevo tratamiento")
        
        #Defining the buttons from the button box
        self.saveButton=self.ui.finalButtons.button(self.ui.finalButtons.StandardButton.Save)
        self.resetButton=self.ui.finalButtons.button(self.ui.finalButtons.StandardButton.Reset)

        #Connecting slots
        self.ui.nameEdit.textEdited.connect(self.nameOnEdit)
        self.ui.firstSurnameEdit.textEdited.connect(self.firstSurnameOnEdit)
        self.ui.secondSurnameEdit.textEdited.connect(self.secondSurnameOnEdit)
        self.ui.birthdayEdit.dateChanged.connect(self.onBirthDayDateChanged)
        #Buttonbox slots
        self.resetButton.clicked.connect(self.onResetPressed)
        self.saveButton.clicked.connect(self.onSavePressed)

        #ComboBox slots
        self.ui.treatmentOptions.currentIndexChanged.connect(self.treatmentIndexChangedSlot)
        self.ui.genderComboBox.currentIndexChanged.connect(self.genderIndexChangedSlot)
        self.ui.technicianComboBox.currentIndexChanged.connect(self.setPhysicistNames)
        self.ui.doctorComboBox.currentIndexChanged.connect(self.setDoctorNames)
        self.ui.treatmentNumber.currentIndexChanged.connect(self.retrieveTreatmentAndWrite)

        #Date events
        self.ui.autofillDate.clicked.connect(self.autofillEventDate)
        self.ui.addDate.clicked.connect(self.onAddDateClicked)

        #Set focus Slots for quicker filling times
        self.ui.historyNumberEdit.returnPressed.connect(self.ui.nameEdit.setFocus)
        self.ui.nameEdit.returnPressed.connect(self.ui.firstSurnameEdit.setFocus)
        self.ui.firstSurnameEdit.returnPressed.connect(self.ui.secondSurnameEdit.setFocus)

        #On edit AN
        self.ui.historyNumberEdit.textEdited.connect(self.checkForClinicNumber)
        #On edit calcretries
        self.ui.calcRetries.textEdited.connect(self.onCalcRetriesEdited)

    #Defining slots functions
    
    def nameOnEdit(self):
        if self.isNameValid(self.ui.nameEdit.text()):
            self.patientData.patientName=self.ui.nameEdit.text()
        else:
            if self.ui.nameEdit.text():
                self.writeFeedback("Nombre no válido", True, True)
            else:
                self.writeFeedback("Nombre no válido", True)

    
    def firstSurnameOnEdit(self):
        if self.isNameValid(self.ui.firstSurnameEdit.text()):
            self.patientData.patientFirstSurname=self.ui.firstSurnameEdit.text()
        else:
            if self.ui.firstSurnameEdit.text():
                self.writeFeedback("Primer apellido no válido", True, True)
            else:
                self.writeFeedback("Primer apellido no válido", True)

    
    def secondSurnameOnEdit(self):
        if self.isNameValid(self.ui.secondSurnameEdit.text()):
            self.patientData.patientSecondSurname=self.ui.secondSurnameEdit.text()
        else:
            if self.ui.secondSurnameEdit.text():
                self.writeFeedback("Segundo apellido no válido", True, True)
            else:
                self.writeFeedback("Segundo apellido no válido", True)

    #On treatment type changed
    def treatmentIndexChangedSlot(self):
        self.patientData.treatmentOption=self.ui.treatmentOptions.currentIndex()

    #On gender changed
    def genderIndexChangedSlot(self):
        self.patientData.patientGender=self.ui.genderComboBox.currentIndex()
    
    #Reset all gaps to make their value null and the variables
    def onResetPressed(self):
        self.restartDemographicField()
        self.restartTreatmentField()

    #save the state of the variables
    def onSavePressed(self):
        self.writeFeedback("Guardando...")
        if self.patientData.patientClinicNumber!=-1:
            if (self.ui.treatmentNumber.count()-1!=self.ui.treatmentNumber.currentIndex()):
                self.patientData.treatmentNumber=self.ui.treatmentNumber.currentIndex()
            self.patientData.doctorsObservation=self.ui.doctorObservationsEdit.toPlainText()
            self.patientData.physiciansObservation=self.ui.physicianObservationsEdit.toPlainText()
            self.patientData.treatmentNumber=self.ui.treatmentNumber.currentIndex()
            self.writeSQL()
            self.writeFeedback("Guardado, recargando base de datos...")
            self.sql.loadTreatmentTable()
            self.loadMatchingTreatments()
            self.ui.treatmentNumber.setCurrentIndex(self.patientData.treatmentNumber)
        else:
            self.writeFeedback("Rellene el número de historial clínico",True, True)

    def checkForClinicNumber(self):
        self.restartDemographicField()
        self.restartTreatmentField()
        if(isValidNUSHA(self.ui.historyNumberEdit.text())):
            self.ui.treatmentNumber.clear()
            self.ui.treatmentNumber.addItem("Nuevo tratamiento")
            obtainedTuple=self.sql.loadDemographicData(int(self.ui.historyNumberEdit.text()))
            if(obtainedTuple):
                self.patientData.fromTupleToDataStructure(obtainedTuple)
                self.writeDemographicVariables()
                self.ui.personalDataFame.setEnabled(False)
                self.loadMatchingTreatments()
                self.writeFeedback("Usuario existente, cargando...")
            else:
                self.writeFeedback("Usuario nuevo, cargando...")
                self.ui.personalDataFame.setEnabled(True)
            self.setDatesVars()
        else:
            self.writeFeedback("Número de historia clínica no válido", True)
            self.ui.personalDataFame.setEnabled(False)

    def writeDemographicVariables(self):
        self.ui.nameEdit.setText(self.patientData.patientName)
        self.ui.firstSurnameEdit.setText(self.patientData.patientFirstSurname)
        self.ui.secondSurnameEdit.setText(self.patientData.patientSecondSurname)
        self.ui.genderComboBox.setCurrentIndex(self.patientData.patientGender)
        self.ui.birthdayEdit.setDate(date.fromordinal(self.patientData.patientBirthday))

    def retrieveTreatmentAndWrite(self):
        self.writeFeedback("Cargando...")
        self.restartTreatmentField()
        self.setDatesVars()
        if (self.ui.treatmentNumber.count()-1!=self.ui.treatmentNumber.currentIndex())and(isValidNUSHA(self.ui.historyNumberEdit.text())):
            self.patientData.fromTupleToDataStructure(self.sql.loadPatientTreatment(self.patientData.patientClinicNumber, 
                self.ui.treatmentNumber.currentIndex()))
            self.writeTreatmentVariables()
        self.writeFeedback("Tratamiento cargado")

    def writeTreatmentVariables(self):
        self.ui.treatmentOptions.setCurrentIndex(self.patientData.treatmentOption)
        self.writeDateListOnTable(self.patientData.datesList)
        self.ui.doctorObservationsEdit.setText(self.patientData.doctorsObservation)
        self.ui.physicianObservationsEdit.setText(self.patientData.physiciansObservation)
        self.ui.calcRetries.setText(str(self.patientData.numberOfCalcTries))
        if(self.patientData.attendingDoctor):
            if self.patientData.attendingDoctor in self.doctorsList:
                self.ui.doctorComboBox.setCurrentIndex(self.doctorsList.index(self.patientData.attendingDoctor))
            else:
                self.ui.doctorComboBox.addItem(self.patientData.attendingDoctor)
                self.ui.doctorComboBox.setCurrentIndex(len(self.doctorsList))
        
        if(self.patientData.attendingRadiophysicist):
            if self.patientData.attendingRadiophysicist in self.techniciansList:
                self.ui.technicianComboBox.setCurrentIndex(self.techniciansList.index(self.patientData.attendingRadiophysicist))
            else:
                self.ui.technicianComboBox.addItem(self.patientData.attendingRadiophysicist)
                self.ui.technicianComboBox.setCurrentIndex(len(self.techniciansList))

    def onBirthDayDateChanged(self):
        self.patientData.patientBirthday=date.fromisoformat(str(self.ui.birthdayEdit.date().toPython())).toordinal()
    
    def autofillEventDate(self):
        self.ui.keyDateEdit.setDate(date.today())
    
    def onAddDateClicked(self):
        self.writeFeedback("Añadiendo fecha...")
        #Adds a date when clicked
        if self.ui.dateType.currentIndex()!=0:      #Checks a type of date was chosen
            if self.ui.dateType.currentIndex()==2:
                self.patientData.beginCalcDate=date.toordinal(self.ui.keyDateEdit.date().toPython())
            if (self.ui.dateType.currentIndex()!=1)and(self.ui.dateType.currentIndex()!=2)and(self.ui.dateType.currentIndex()!=3):
                timeElapsed=date.toordinal(self.ui.keyDateEdit.date().toPython())-self.patientData.beginCalcDate
            else:
                timeElapsed=0
            self.writeDateItem(self.ui.dateType.currentIndex(), 
                self.ui.keyDateEdit.date().toPython(), 
                timeElapsed)
            self.ui.dateType.setCurrentIndex(0)
            self.writeFeedback("Fecha añadida")
        else:
            self.writeFeedback("Tipo de fecha no escogida",True , True)
        self.patientData.datesList=self.readDatesOfDateComboBox()
    
    def writeDateListOnTable(self, dateList):
        #Writes datelist in the table
        for i in dateList:
            self.writeDateItem(i[0], i[1], i[2], False)

    def readDatesOfDateComboBox(self):
        #Reads the combobox and creates a list of tuples containing the dates
        dateList=[]
        for i in range(self.ui.dateTableView.rowCount()):
            dateTuple=(self.DATE_OPTIONS.index(self.ui.dateTableView.item(i,0).text()),
                toOrdinal(self.ui.dateTableView.item(i,1).text(), True), 
                self.ui.dateTableView.item(i,2).text())
            dateList.append(dateTuple)
        return dateList

    def writeDateItem(self, typeOfDate, itemDate, daysFromReception=0, validate=True):
        #Check whether the dates are introduced in good order and writes them
        writeable=False
        if (type(itemDate)==int):
            ordinalDate=itemDate
        else:
            ordinalDate=date.fromisoformat(str(itemDate)).toordinal()
        #Checks that user doesn't add a date in an erroneus order
        match typeOfDate:       #Writes the variables storing the different dates
            case 1:
                if not(self.hasRequest):
                    writeable=True
                    self.hasRequest=True
            case 2:
                if (self.hasRequest)and(not(self.hasCompleteReception)):
                    writeable=True
                    self.hasCompleteReception=True
            case 3:
                if (self.hasRequest)and(not(self.hasCompleteReception)):
                    writeable=True
            case 4:
                if (self.hasCompleteReception)and(not(self.hasCalcEnd)):
                    writeable=True
            case 5:
                if (self.hasCompleteReception)and(not(self.hasCalcEnd)):
                    writeable=True
                    self.hasCalcEnd=True
            case 6:
                if (self.hasCalcEnd):
                    writeable=True
                    self.hasEmision=True
        if validate:
            if ordinalDate>=self.previousDate:          #Checks if the new date is as recent or more than the previous one
                if writeable:
                    rowNumber=self.ui.dateTableView.rowCount()
                    self.ui.dateTableView.insertRow(rowNumber)
                    self.ui.dateTableView.setItem(rowNumber, 0, QTableWidgetItem(self.DATE_OPTIONS[typeOfDate]))
                    self.ui.dateTableView.setItem(rowNumber, 1, QTableWidgetItem(toSpanishDate(itemDate)))
                    self.ui.dateTableView.setItem(rowNumber, 2, QTableWidgetItem(str(daysFromReception)))
                    self.previousDate=ordinalDate
                else:
                    self.writeFeedback("No se puede escribir la fecha, compruebe el orden de las fechas",True,True)
            else:
                self.writeFeedback("La nueva fecha no puede ser más antigua que la previa",True,True)
        else:
            rowNumber=self.ui.dateTableView.rowCount()
            self.ui.dateTableView.insertRow(rowNumber)
            self.ui.dateTableView.setItem(rowNumber, 0, QTableWidgetItem(self.DATE_OPTIONS[typeOfDate]))
            self.ui.dateTableView.setItem(rowNumber, 1, QTableWidgetItem(toSpanishDate(itemDate)))
            self.ui.dateTableView.setItem(rowNumber, 2, QTableWidgetItem(str(daysFromReception)))


    def setPhysicistNames(self):
        #On change physicist set variable in patientData
        if self.ui.technicianComboBox.currentIndex()!=0:
            self.patientData.attendingRadiophysicist=self.techniciansList[self.ui.technicianComboBox.currentIndex()]
        else:
            self.patientData.attendingRadiophysicist=""
    
    def setDoctorNames(self):
        #On change physicist set variable in patientData
        if self.ui.doctorComboBox.currentIndex()!=0:
            self.patientData.attendingDoctor=self.doctorsList[self.ui.doctorComboBox.currentIndex()]
        else:
            self.patientData.attendingDoctor=""

    def restartTreatmentField(self):
        #Resets all treatment related widgets
        self.ui.dateTableView.setRowCount(0)
        self.ui.doctorComboBox.clear()
        self.getDoctorsList()
        self.ui.doctorComboBox.addItems(self.doctorsList)
        self.ui.technicianComboBox.clear()
        self.getTechniciansList()
        self.ui.technicianComboBox.addItems(self.techniciansList)
        self.ui.treatmentOptions.setCurrentIndex(0)
        self.ui.doctorObservationsEdit.clear()
        self.ui.physicianObservationsEdit.clear()
        self.ui.calcRetries.setText("1")
    
    def restartDemographicField(self):
        #Resets all demographic related widgets
        self.ui.nameEdit.clear()
        self.ui.firstSurnameEdit.clear()
        self.ui.secondSurnameEdit.clear()

    def onCalcRetriesEdited(self):
        #Checks if the calc retries is a number and sets it in the patient data
        if(self.ui.calcRetries.text().isnumeric()):
            self.patientData.numberOfCalcTries=int(self.ui.calcRetries.text())
        else:
            self.ui.calcRetries.clear()

    def loadMatchingTreatments(self):
        #Loads all the matching treatments for a AN number for user to choose the treatment
        numberOfMatchingTreatments=len(self.sql.loadPatientTreatment(self.ui.historyNumberEdit.text()))
        self.ui.treatmentNumber.clear()
        for i in range(1, numberOfMatchingTreatments+1):
            self.ui.treatmentNumber.addItem(str(i))
            #Adds the options to combobox
        self.ui.treatmentNumber.addItem("Nuevo tratamiento")
        self.ui.treatmentNumber.setCurrentIndex(numberOfMatchingTreatments)

    def writeFeedback(self, message, error=False, dialog=False):
        #Writes feedback in feedback label and adds color and "ERROR:"
        if error:
            self.ui.feedBackLabel.setText("ERROR: ¡"+message+"!")
            self.ui.feedBackLabel.setStyleSheet("color: red")
        else:
            self.ui.feedBackLabel.setText(message)
            self.ui.feedBackLabel.setStyleSheet("color: black")
        if dialog:
            #Creates a dialog if necessary
            self.dialog=dialogActivity(message)