from libs.patientDataStructure import patientDataStructure
from libs.MySQLdb import MySQLdb
from libs.funcs import printProgressBar, inputLogin
from random import randint
import gender_guesser.detector as gender
from libs.globalVars import GENDER_GUESSER_DICT, TREATMENT_OPTIONS
from datetime import date

def getRandomName(nameList, surnameList):
    return nameList[randint(0, len(nameList)-1)]+" "+surnameList[randint(0, len(surnameList)-1)]+" "+surnameList[randint(0, len(surnameList)-1)]

if __name__ == "__main__":
    print("Cargando lista de datos...")
    f=open("names.txt")
    names=[]
    for line in f:
        if line:
            names.append(line)
    f.close()
    f=open("surnames.txt")
    surnames=[]
    for line in f:
        if line:
            surnames.append(line)
    print("Lista de datos cargada...")
    sql=MySQLdb(inputLogin())
    dataNum=int(input("¿Cuantos datos quieres introducir? "))
    d=gender.Detector(False)
    sql.connectToDemographicDB()
    sql.connectToTreatmentDB()
    for i in range(0, dataNum):
        patientData=patientDataStructure()
        printProgressBar(i, dataNum)    #Progress
        patientData.patientClinicNumber=randint(0, 1000000000)
        #Patient data
        patientData.patientName=names[randint(0, len(names)-1)]
        patientData.patientFirstSurname=surnames[randint(0, len(surnames)-1)]
        patientData.patientSecondSurname=surnames[randint(0, len(surnames)-1)]
        patientData.patientGender=GENDER_GUESSER_DICT[str(d.get_gender(patientData.patientName))]
        patientData.patientBirthday=randint(date.today().toordinal()-100*365, date.today().toordinal())
        #Treatment
        patientData.attendingDoctor=getRandomName(names, surnames)
        patientData.attendingRadiophysicist=getRandomName(names, surnames)
        patientData.treatmentOption=randint(0, len(TREATMENT_OPTIONS)-1)
        patientData.numberOfCalcTries=randint(1, 10)
        patientData.doctorsObservation=""
        patientData.physiciansObservation=""
        actualDate=randint(date.today().toordinal()-10*365, date.today().toordinal())
        patientData.datesList.append((1, actualDate, 0))
        actualDate+=randint(0, 5)
        completeReception=actualDate
        patientData.datesList.append((2, actualDate, 0))
        for i in range(0, randint(0, 3)):
            actualDate+=randint(0, 5)
            patientData.datesList.append((4, actualDate, actualDate-completeReception))
        actualDate+=randint(0, 5)
        patientData.datesList.append((5, actualDate, actualDate-completeReception))
        actualDate+=randint(0, 5)
        #Save data
        patientData.datesList.append((6, actualDate, actualDate-completeReception))
        sql.saveDemographicData(patientData.fromVarToDemographicTuple())
        sql.saveTreatmentData(patientData.fromVarToTreatmentTuple())
