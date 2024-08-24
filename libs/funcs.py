from datetime import date
from datetime import datetime

def toSpanishDate(unformattedDate):
    if type(unformattedDate) is int:
        return date.fromordinal(unformattedDate).strftime("%d-%m-%Y")
    elif type(unformattedDate) is date:
        return unformattedDate.strftime("%d-%m-%Y")

def toOrdinal(unformattedDate, spanish=False):
    if spanish:
        dateList=unformattedDate.split("-")
        ordinalDate=date.fromisoformat(dateList[2]+"-"+dateList[1]+"-"+dateList[0]).toordinal()     #YYYY-MM-DD
        return ordinalDate
    elif type(unformattedDate) is date:
        return unformattedDate.toordinal()

def isValidNUSHA(nusha):
    return (len(nusha)==10)and(nusha.isnumeric())

def formatNUSHA(nusha):
    if len(nusha)==9:
        return "0"+nusha
    else:
        return nusha