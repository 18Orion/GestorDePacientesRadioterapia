import mysql.connector
import json

class MySQLdb(object):
    """
    A class to manage the conections to MySQL stablish connections to both databases and tables.
    It manages the initial connections and the creation of databases and tables
    """
    def __init__(self, credentials):
        #Define host, user and name for connections
        if not(credentials):
            self.loadJsonConf()
        else:
            self.host='localhost'
            self.user=credentials[0]
            self.password=credentials[1]
        #Defining databases and their subsequent tables
        self.demographicDBTuple=("demographicDB", "demographicData")        #DB, table
        self.treatmentDBTuple=("treatmentDB","treatmentData")               #DB, table

    def __del__(self):
        pass
    
    #Defining json reading function for loading configuration
    def loadJsonConf(self):
        #loads the configuration under SQL.json
        f=open("SQL.json")
        data=json.load(f)
        for i in data["sql_connection"]:
            self.host=i["host"]
            self.user=i["user"]
            self.password=i["password"]
        f.close()

    #Defining standard and database independent functions

    def listAvaiableDB(self):
        #Function that connects to MySQL and lists all avaiable DBs yielding them
        checkConnection=mysql.connector.connect(host=self.host,
                user=self.user,
                password=self.password)
        listDB=checkConnection.cursor()
        listDB.execute("SHOW DATABASES")
        for i in listDB:
            yield i[0]

    def databaseExists(self, dataBaseName):
        #Checks wether a database exists or not given a list of DBs provided by self.listAvaiableDB()
        for yieldedDB in self.listAvaiableDB():
            if yieldedDB==dataBaseName:
                return True
        return False
    
    def connectToDB(self, nameDB):
        """
        Connects to a database yielding  the database class, the subsequent cursor and wether the 
        database already existed.
        """
        DBexists=self.databaseExists(nameDB)        #Checks the existance of the DB
        if DBexists:
            DB=mysql.connector.connect(host=self.host,  #Creates the DB class
                user=self.user,
                password=self.password, 
                database=nameDB)
            cursor=DB.cursor()  #Creates the cursor
        else:
            DB=mysql.connector.connect(host=self.host,
                user=self.user,
                password=self.password)
            cursor=DB.cursor()
            cursor.execute("CREATE DATABASE "+nameDB)   #Creates the DB
            DB=mysql.connector.connect(host=self.host,  #Creates the DB class
                user=self.user,
                password=self.password, 
                database=nameDB)
            cursor=DB.cursor()          #Creates the cursor
        yield DB        #yields database
        yield cursor    #yields cursor
        yield DBexists  #Yields wether database already existed
    
    def loadTableFromDatabase(self, cursorClass, tableName):
        #Function to load a table froma a database, given the database's cursor class and the table name
        cursorClass.execute("SELECT * FROM "+tableName)
        return cursorClass.fetchall()

    #End of definition of strandard functions
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
        if not(next(connectionTry)):      #Checks if the DB was created and if not populates it with a table  
            self.demographicInterface.execute("CREATE TABLE "+self.demographicDBTuple[1]+" (AN INT UNSIGNED,\
                Name VARCHAR(50), \
                First_Surname VARCHAR(50), \
                Second_Surname VARCHAR(50), \
                Birthday INT UNSIGNED, \
                Gender TINYINT UNSIGNED)")
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
        if not(next(connectionTry)):      #Checks if the DB was created and if not populates it with a table  
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
    
    def overwriteTreatmentData(self, treatmentTuple, AN, treatmentNumber):
        self.treatmentInterface.execute("UPDATE "+self.treatmentDBTuple[1]+ "SET\
            Clinic_Number=%s, \
            Treatment_Number=%s, \
            Dates=%s, \
            Calc_Time=%s, \
            Treatment_Option=%s, \
            Attending_Doctor=%s, \
            Attending_Physician=%s, \
            Doctors_Observation=%s, \
            Physicians_Observation=%s,\
            Calc_Tries=%s)", treatmentTuple)
        self.treatmentDB.commit()
