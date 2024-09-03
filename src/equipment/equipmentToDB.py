from libs.MySQLdb import MySQLdb
from datetime import date
from libs.confReader import confReader
from libs.funcs import getNameListFromFile

class equipmentToDB(object):
    def __init__(self):
        conf=confReader()
        self.sql=MySQLdb(self.credentials)
        self.sql.connectToEquipmentDB()
        self.sql.connectToMantainenementDB()
        self.brands=self.getBrandList()
        self.models=[]
        self.serialNumbers=[]
        self.technicians=getNameListFromFile(conf.techniciansFile, 
            "#En este archivo se definen los nombres de los técnicos que figuran en el programa")
        self.radiophysicist=getNameListFromFile(conf.physicistFile, 
            "#En este archivo se definen los nombres de los radiofísicos que figuran en el programa")

    def getBrandList(self):
        brandList=["Sin escoger"]
        for i in self.sql.equipmentTable:
            if not(i[0] in brandList):
                brandList.append(i[0])
        return brandList
    
    def getModels(self, brand):
        modelList=["Sin escoger"]
        for i in self.sql.equipmentTable:
            if i[0]==brand and not(i[1] in modelList):
                modelList.append(i[1])
        return modelList
    
    def getSerials(self, brand, model):
        serialsList=["Sin escoger"]
        for i in self.sql.equipmentTable:
            if i[0]==brand and i[1]==model and not(i[2] in serialsList):
                serialsList.append(i[2])
        return serialsList
    
    def getComment(self, brand, model, serialNumber):
        for i in self.sql.equipmentTable:
            if i[0]==brand and i[1]==model and i[2]==serialNumber:
                return i[3]

    def getMatchingOperations(self, serial):
        matchingOperations=[]
        if self.sql.mantainementTable:
            for i in self.sql.mantainementTable:
                if i[0]==serial:
                    matchingOperations.append(i)
        return matchingOperations