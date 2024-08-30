#The treatment is stored as an integer called "typeOfTreatment" in which  the integers value shows 
#which treatment the patient recieved
#   0. No escogido
#   1. 3D
#   2. VMAT
#   3. IMRT
#   4. ICT
#   5. BQ
#   6. Urgencia

#The dates are saved as integers representing the number of days since day 1 year 1 AD

#Clinic history numbers are stored as a 10 digit integer without the extension "AN"

#For each different treatment for a patient the treatment number stores the chronological order

#Gender is stored in the same way as the type of treatment
#   0. Male
#   1. Female

#Dates are saved in a list of tuples which saves both the type of date and the date itself,
#where:
#   0.  No escogido
#   1.  Solicitud
#   2.  Recepción completa
#   3.  Recepción incompleta
#   4.  QA
#   5.  Emisión
#So when added the tuple looks like this: (2, 8292340)

class patientDataStructure(object):
    """
    A class to save patient data with a structure and their own functions.
    This functions include going from structure to tuple in order to acommodate
    functionality for SQL
    """
    def __init__(self):
        #Defining patient data structure
        self.patientClinicNumber=-1      #Clinic number is shared across both tuples
        #Demographic tuple's variables in order
        self.patientName=""
        self.patientFirstSurname=""
        self.patientSecondSurname=""
        self.patientBirthday=0
        self.patientGender=0
        #Treatment tuple's variable in order
        self.treatmentNumber=0
        self.datesList=[]
        self.treatmentOption=0
        self.attendingDoctor=""
        self.attendingRadiophysicist=""
        self.doctorsObservation=""
        self.physiciansObservation=""
        self.numberOfCalcTries=0
        #Demographic tuple consists in four variables whereas treatment tuple has six variables
        #Begin and end calc dates extracted
        self.beginCalcDate=0
    
    def fromVarToDemographicTuple(self):
        #Function to convert data structure into SQL readable tuple
        return (self.patientClinicNumber, 
            self.patientName, 
            self.patientFirstSurname, 
            self.patientSecondSurname, 
            self.patientBirthday, 
            self.patientGender)

    def fromVarToTreatmentTuple(self):
        #Function to convert data structure into SQL readable tuple
        return (self.patientClinicNumber,
            self.treatmentNumber, 
            self.fromDateListToSQLString(),
            self.treatmentOption,
            self.attendingDoctor,
            self.attendingRadiophysicist,
            self.doctorsObservation,
            self.physiciansObservation,
            self.numberOfCalcTries)
    
    def fromTupleToDataStructure(self, dataTuple):
        #Function to go from either type of tuple to data structure
        if len(dataTuple)==6:
            self.patientClinicNumber=dataTuple[0]
            self.patientName=dataTuple[1]
            self.patientFirstSurname=dataTuple[2]
            self.patientSecondSurname=dataTuple[3]
            self.patientBirthday=dataTuple[4]
            self.patientGender=dataTuple[5]
        elif len(dataTuple)==9:
            self.patientClinicNumber=dataTuple[0]
            self.treatmentNumber=dataTuple[1]
            self.datesList=self.fromSQLStringToDateList(dataTuple[2])
            self.treatmentOption=dataTuple[3]
            self.attendingDoctor=dataTuple[4]
            self.attendingRadiophysicist=dataTuple[5]
            self.doctorsObservation=dataTuple[6]
            self.physiciansObservation=dataTuple[7]
            self.numberOfCalcTries=dataTuple[8]
            
    def resetVariables(self):
        #Reset all variables
        self.patientClinicNumber=0
        self.patientName=""
        self.patientFirstSurname=""
        self.patientSecondSurname=""
        self.treatmentNumber=0
        self.beginCalcDate=0
        self.endCalcDate=0
        self.treatmentOption=0

    def editDate(self, dateTuple, listIndex=None):
        if listIndex==None:
            self.datesList.append(dateTuple)
        else:
            self.datesList[listIndex]=dateTuple

    def fromDateListToSQLString(self):
        #Transforms a DateList into a SQL compatible string
        SQLString=""
        for i in range(len(self.datesList)):
            addingTuple=self.datesList[i]
            SQLString+=str(addingTuple[0])+':'+str(addingTuple[1])+':'+str(addingTuple[2])
            if i!=(len(self.datesList)-1):
                SQLString+=','
        return SQLString.replace(' ','')
    
    def fromSQLStringToDateList(self, SQLString):
        #Transform a string retrieved from SQL to a DateList
        rawList=str(SQLString).split(",")
        processedList=[]
        for i in rawList:
            dateSplit=i.split(":")
            typeOfDate=int(dateSplit[0])
            date=int(dateSplit[1])
            daysFromReception=int(dateSplit[2])
            processedTuple=(typeOfDate, date, daysFromReception)
            processedList.append(processedTuple)
            #Populates the variables which are important 
            if typeOfDate==2:
                self.beginCalcDate=date
        return processedList
