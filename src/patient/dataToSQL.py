from datetime import date
from libs.MySQLdb import MySQLdb
from libs.patientDataStructure import patientDataStructure
from libs.globalVars import *
from libs.confReader import confReader
from libs.funcs import getNameListFromFile

class dataToSQL(object):
    def __init__(self):
        self.sql=MySQLdb(credentials=self.credentials)
        #Connect to databases
        self.sql.connectToDemographicDB()
        self.sql.connectToTreatmentDB()
        self.conf=confReader()
        #Create patient data structure        
        self.patientData=patientDataStructure()
        #Create lists
        self.getPhysicistsList()       #Reads config for physicians' list
        self.getDoctorsList()           #Reads config for doctors' list
        self.matchingTreatmentOptions=["Nuevo tratamiento"]
        #Set booleans
        self.previousDate=0

    def getPhysicistsList(self):
        #Get physicist name list
        self.radiophysicistList=getNameListFromFile(self.conf.physicistFile, 
            "#En este archivo se definen los nombres de los radiofísicos que figuran en el programa\n")

    def getDoctorsList(self):
        #Get doctor name list
        self.doctorsList=getNameListFromFile(self.conf.doctorsFile,
            "#En este archivo se definen los nombres de los doctores que figuran en el programa\n")

    def writeSQL(self):
        #Writes the sql data
        self.sql.saveDemographicData(self.patientData.fromVarToDemographicTuple())
        self.sql.saveTreatmentData(self.patientData.fromVarToTreatmentTuple())
    
    def isNameValid(self, name=""):
        #Checks if the name is acceptable
        if (name!="")and(name.replace(" ", "").isalpha()):
            return True
        else: 
            print("Error: Name or surname not valid")
            return False

    def calculateTimeElapsed(self, ordinalDate):
        #Calculates the elapsed time from complete reception
        return int(ordinalDate-self.patientData.beginCalcDate)