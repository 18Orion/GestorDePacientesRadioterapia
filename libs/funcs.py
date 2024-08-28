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

def inputLogin():
    user=input("Usuario: ")
    passwd=input("Contraseña: ")
    cred=(user, passwd)
    return cred

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()