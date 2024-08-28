import requests
from platform import system
from urllib.request import urlretrieve
version = (requests.get("https://github.com/18Orion/GestorDePacientesRadioterapia/releases/latest").url.split("/").pop(), system())
print("Descargando version "+version[0]+" para la plataforma "+version[1])
if version[1]=="Linux":
    urlretrieve("https://github.com/18Orion/GestorDePacientesRadioterapia/releases/latest/download/linuxRelease.zip", "release.zip")
elif version[1]=="Windows":
    urlretrieve("https://github.com/18Orion/GestorDePacientesRadioterapia/releases/latest/download/winRelease.zip", "release.zip")
