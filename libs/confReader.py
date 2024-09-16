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
        for programData in data["UI"]:
            self.phrase=programData["frasemenu"]
            self.patients=programData["pacientes"]
            self.equipment=programData["equipos"]
        for filesData in data["files"]:
            self.doctorsFile=filesData["medicos"]
            self.physicistFile=filesData["radiofisicos"]
            self.techniciansFile=filesData["tecnicos"]
            self.centreFile=filesData["centro"]
            self.serviceFile=filesData["servicio"]
            self.brandsFile=filesData["marcas"]
        for sqlData in data["SQL"]:
            self.host=sqlData["host"]
            self.demographicDBTuple=(str(sqlData["baseDatosDemografica"]), str(sqlData["tablaDemografica"]))
            self.treatmentDBTuple=(str(sqlData["baseDatosTratamiento"]), str(sqlData["tablaTratamiento"]))
            self.equipmentDBTuple=(str(sqlData["baseDatosEquipos"]),str(sqlData["tablaEquipos"]))
            self.mantainementDBTuple=(str(sqlData["baseDatosMantenimiento"]),str(sqlData["tablaMantenimiento"]))