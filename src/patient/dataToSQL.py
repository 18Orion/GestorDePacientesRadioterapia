from datetime import date
from libs.MySQLdb import MySQLdb
from libs.patientDataStructure import patientDataStructure
from libs.globalVars import *

class dataToSQL(object):
    def __init__(self):
        self.sql=MySQLdb(credentials=self.credentials)
        #Connect to databases
        self.sql.connectToDemographicDB()
        self.sql.connectToTreatmentDB()
        #Create patient data structure        
        self.patientData=patientDataStructure()
        #Create lists
        self.TREATMENT_OPTIONS=TREATMENT_OPTIONS                                #Constant
        self.GENDER_OPTIONS=GENDER_OPTIONS                                      #Constant
        self.DATE_OPTIONS=DATE_OPTIONS                                          #Constant
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
