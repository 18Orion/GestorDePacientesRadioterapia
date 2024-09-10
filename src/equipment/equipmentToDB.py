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
        self.sql.loadEquipmentTable()
        self.sql.loadMantainementTable()
        self.operationNumber=0
        self.models=[]
        self.serialNumbers=[]
        self.technicians=getNameListFromFile(conf.techniciansFile, 
            "#En este archivo se definen los nombres de los técnicos que figuran en el programa")
        self.radiophysicist=getNameListFromFile(conf.physicistFile, 
            "#En este archivo se definen los nombres de los radiofísicos que figuran en el programa")
        self.params=["Sin escoger"] * 6

    def getMatching(self, pattern, tupleIndex, tupleList):
        if pattern!="Sin escoger" and pattern:
            filteredList=[]
            for iTuple in tupleList:
                if iTuple[tupleIndex]==pattern:
                    filteredList.append(iTuple)
            return filteredList
        else:
            return tupleList

    def getAllPosibilities(self, tupleIndex, tupleList):
        posibilitiesList=["Sin escoger"]
        for i in tupleList:
            if not(i[tupleIndex] in posibilitiesList):
                posibilitiesList.append(i[tupleIndex])
        return posibilitiesList

    def searchBy(self):
        filteredList=self.sql.equipmentTable
        newList=[]
        for index in range(len(self.params)):
            if self.params[index]!="Sin escoger":
                filteredList=self.getMatching(self.params[index], index, filteredList)
            else:
                finalIndex=index
                break
        yield filteredList
        yield self.getAllPosibilities(finalIndex, filteredList)

    def setParam(self, param, index):
        self.params[index]=param
        for i in range(index+1, len(self.params)):
            self.params[i]="Sin escoger"

    def getMatchingOperations(self, serial):
        matchingOperations=[]
        if self.sql.mantainementTable:
            for i in self.sql.mantainementTable:
                if i[0]==serial:
                    matchingOperations.append(i)
        return matchingOperations