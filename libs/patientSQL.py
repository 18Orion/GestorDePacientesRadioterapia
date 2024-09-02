from libs.MySQLdb import MySQLdb

class patientSQL(object, MySQLdb):
    def __init__(self, credentials):
        super.__init__(credentials)
        self.demographicDBTuple=conf.demographicDBTuple           #DB, table
        self.treatmentDBTuple=conf.treatmentDBTuple               #DB, table

    #Defining demographic database specific functions, essentially wrappers

    def connectToDemographicDB(self):
        """
        Connects to demographiDB with standard function and creates a table if DB did not exists
        It is essentially a wrapper of the standard connection function of this class, adding 
        other neccessary actions
        """
        connectionTry=self.connectToDB(self.demographicDBTuple[0])
        self.demographicDB=next(connectionTry)
        self.demographicInterface=next(connectionTry)
        #if not(next(connectionTry))or(not(self.tableExists(self.demographicInterface, self.demographicDBTuple[1]))):      #Checks if the DB was created and if not populates it with a table  
        try:
            self.demographicInterface.execute("CREATE TABLE "+self.demographicDBTuple[1]+" (AN INT UNSIGNED,\
                Name VARCHAR(50), \
                First_Surname VARCHAR(50), \
                Second_Surname VARCHAR(50), \
                Birthday INT UNSIGNED, \
                Gender TINYINT UNSIGNED)")
        except:
            pass
        self.loadDemographicTable()

    def loadDemographicTable(self):
        #Function to load the table from demographic database
        self.demographicTable=self.loadTableFromDatabase(self.demographicInterface, self.demographicDBTuple[1])
    
    def clinicNumberExists(self, clinicNumber):
        for i in range(len(self.demographicTable)):
            if self.demographicTable[i][0]==int(clinicNumber):
                return True
        return False

    def saveDemographicData(self, patientTuple):
        if not(self.clinicNumberExists(patientTuple[0])):
            self.demographicInterface.execute("INSERT INTO "+self.demographicDBTuple[1]+" VALUES (%s,%s,%s,%s,%s,%s)", patientTuple)
            self.demographicDB.commit()
        else:
            pass
            #print("Number already exists")

    def loadDemographicData(self, clinicNumber):
        for patientTuple in self.demographicTable:
            if patientTuple[0]==clinicNumber:
                return patientTuple

    #End of definition of demographic database specific functions
    #Defining treatment database specific functions

    def connectToTreatmentDB(self):
        connectionTry=self.connectToDB(self.treatmentDBTuple[0])
        self.treatmentDB=next(connectionTry)
        self.treatmentInterface=next(connectionTry)
        #Checks if the DB was created and if not populates it with a table  
        try:
            self.treatmentInterface.execute("CREATE TABLE "+self.treatmentDBTuple[1]+" (\
                Clinic_Number INT UNSIGNED, \
                Treatment_Number TINYINT UNSIGNED, \
                Dates TEXT, \
                Treatment_Option TINYINT UNSIGNED, \
                Attending_Doctor VARCHAR(100), \
                Attending_Physician VARCHAR(100), \
                Doctors_Observation LONGTEXT, \
                Physicians_Observation LONGTEXT,\
                Calc_Tries TINYINT UNSIGNED)")
        except:
            pass
        self.loadTreatmentTable()

    def loadTreatmentTable(self):
        self.treamentTable=self.loadTableFromDatabase(self.treatmentInterface, self.treatmentDBTuple[1])

    def loadPatientTreatment(self, AN, treatmentNumber=None):
        if treatmentNumber==None:
            matchingTreatmentsList=[]
            for treatment in self.treamentTable:
                if treatment[0]==int(AN):
                    matchingTreatmentsList.append(treatment)
            return matchingTreatmentsList
        else:
            for treatment in self.treamentTable:
                if (treatment[0]==int(AN))and(treatment[1]==int(treatmentNumber)):
                    return treatment

    def saveTreatmentData(self, treatmentTuple):
        try:
            self.treatmentInterface.execute("DELETE FROM "+self.treatmentDBTuple[1]+" WHERE Clinic_Number=%s AND Treatment_Number=%s", (treatmentTuple[0], treatmentTuple[1]))
            self.treatmentDB.commit()
            #print("Overwriting")
        except:
            pass
        self.treatmentInterface.execute("INSERT INTO "+self.treatmentDBTuple[1]+" VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", treatmentTuple)
        self.treatmentDB.commit()
    
    #End of definition of treatment database specific functions