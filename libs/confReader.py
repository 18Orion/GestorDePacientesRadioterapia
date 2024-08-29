import json

class confReader(object):
    def __init__(self):
        self.loadJsonConf()

    def loadJsonConf(self):
        #loads the configuration under SQL.json
        f=open("configuration.json")
        data=json.load(f)
        f.close()
        for programData in data["program"]:
            self.version=programData["version"]
            self.pythonVersion=programData["pythonVersion"]
            self.mysql=programData["mysql"]
            
        for filesData in data["files"]:
            self.doctorsFile=filesData["medicos"]
            self.physicistFile=filesData["radiofisicos"]

        for sqlData in data["SQL"]:
            self.host=sqlData["host"]
            self.demographicDBTuple=(str(sqlData["baseDatosDemografica"]), str(sqlData["tablaDemografica"]))
            self.treatmentDBTuple=(str(sqlData["baseDatosTratamiento"]), str(sqlData["tablaTratamiento"]))