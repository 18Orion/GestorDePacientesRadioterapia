import requests
from platform import system
from urllib.request import urlretrieve

def update(packageType, version="latest"):
    if version=="latest":
        version = (requests.get("https://github.com/18Orion/GestorDePacientesRadioterapia/releases/latest").url.split("/").pop(), system())
    else:
        version = (version, system())
    print("Descargando version "+version[0]+" para la plataforma "+version[1])
    match packageType:
        case "source":
            sourceName="GestorDePacientesRadioterapia"+"-"+version[0].replace("v", "")+".zip"
            urlretrieve("https://github.com/18Orion/GestorDePacientesRadioterapia/archive/refs/tags/"+version[0]+".zip", "source.zip")
        case "compiled":
            if version[1]=="Linux":
                urlretrieve("https://github.com/18Orion/GestorDePacientesRadioterapia/releases/latest/download/linuxRelease.zip", "release.zip")
            elif version[1]=="Windows":
                urlretrieve("https://github.com/18Orion/GestorDePacientesRadioterapia/releases/latest/download/winRelease.zip", "release.zip")

if __name__=="__main__":
    version=input("Descargar version (dejar en blanco para la última): ")
    if not(version):
        version="latest"
    match int(input("Descargar 1. Paquete o 2. Source: ")):
        case 1:
            update("compiled", version)
        case 2:
            update("source", version)