from datetime import date
from .MySQLdb import MySQLdb
from .patientDataStructure import patientDataStructure

class dataToSQL(object):
    def __init__(self):
        self.sql=MySQLdb(credentials=self.credentials)
        #Connect to databases
        self.sql.connectToDemographicDB()
        self.sql.connectToTreatmentDB()
        #Create patient data structure        
        self.patientData=patientDataStructure()
        #Create lists
        self.TREATMENT_OPTIONS=["Sin escoger","3D","VMAT","IMRT","ICT","BQ-C", "BQ-F","Urgencia"]     #Constant
        self.GENDER_OPTIONS=["Masculino", "Femenino"]                                       #Constant
        self.DATE_OPTIONS=["Sin escoger", 
            "Solicitud", 
            "Recepción completa", 
            "Recepción incompleta",
            "QA",
            "Fin del calculo",
            "Emisión"]
        self.getTechniciansList()       #Reads config for physicians' list
        self.getDoctorsList()           #Reads config for doctors' list
        self.matchingTreatmentOptions=["Nuevo tratamiento"]
        #Set booleans
        self.setDatesVars()
    
    def setDatesVars(self):
        self.previousDate=0
        self.hasRequest=False
        self.hasCompleteReception=False
        self.hasCalcEnd=False
        self.hasEmision=False

    def getTechniciansList(self):
        f=open("tecnicos.cfg","r")
        self.techniciansList=["Sin escoger"]
        for line in f:
            if line[0]!='#':
                self.techniciansList.append(line.replace("\n",""))

    def getDoctorsList(self):
        f=open("medicos.cfg","r")
        self.doctorsList=["Sin escoger"]
        for line in f:
            if line[0]!='#':
                self.doctorsList.append(line.replace("\n",""))

    def writeSQL(self):
        self.sql.saveDemographicData(self.patientData.fromVarToDemographicTuple())
        self.sql.saveTreatmentData(self.patientData.fromVarToTreatmentTuple())

    def calculateTimeElapsed(self):
        if (self.patientData.endCalcDate!=0)and(self.patientData.beginCalcDate!=0):
            timeElapsed=self.patientData.endCalcDate-self.patientData.beginCalcDate
            if(timeElapsed>=0):
                self.patientData.calcTime=timeElapsed
            else:
                print("Error: Time cannot be negative")
    
    def setHistory(self, clinicNumber=""):              #Returns wether the number is valid or not and saves it
        if (len(clinicNumber)==10)and(clinicNumber.isnumeric()):
            self.patientData.patientClinicNumber=int(clinicNumber)
            return True
        else:
            return False
    
    def isNameValid(self, name=""):
        if (name!="")and(name.replace(" ", "").isalpha()):
            return True
        else: 
            print("Error: Name or surname not valid")
            return False
