from libs.MySQLdb import MySQLdb
from datetime import date

class equipmentToDB(object):
    def __init__(self):
        self.sql=MySQLdb(self.credentials)
        self.sql.connectToEquipmentDB()
        self.brands=self.getBrandList()
        self.models=[]
        self.serialNumbers=[]

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
