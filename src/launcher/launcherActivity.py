# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from libs.confReader import confReader
from .launcherUI import Ui_launcher

#Import all activities
from src.patient.patientActivity import patientActivity     #Introducing patient data
from src.exploit.exploitActivity import exploitActivity     #Exporting data
from src.credentials.credentialsActivity import credentialsActivity
from src.userCreator.userCreatorActivity import userCreatorActivity
from PySide6.QtGui import QPixmap
from libs.funcs import update, getLatestVersion, getVersionInt
from src.dialog.dialogActivity import dialogActivity
from multiprocessing import Process
from os import listdir
from src.equipment.equipmentActivity import equipmentActivity
from src.equipmentRegistration.equipmentRegistrationActivity import equipmentRegistrationActivity
from src.about.aboutActivity import aboutActivity
from sys import exit

class launcherActivity(QMainWindow):
    def __init__(self, credentials, parent=None):
        super().__init__(parent)
        self.ui = Ui_launcher()
        self.ui.setupUi(self)
        #SQL conf
        self.credentials=credentials
        #UI configuration
        self.conf=confReader()
        self.ui.name.setText(credentials[0])                            #Set user
        self.ui.version.setText(self.conf.version)                      #Set version in label
        self.ui.juntaAnd.setPixmap(QPixmap(u"./assets/logo.jpg"))       #Put logo in launcher
        self.ui.userCreatorLaunch.setEnabled(credentials[0]=="root")    #Only allow root to create a new user
        self.updatable=0
        #Define slots
        self.ui.patientUILaunch.clicked.connect(self.launchPatient)
        self.ui.exportUILaunch.clicked.connect(self.launchExport)
        self.ui.changeCredentialsUILaunch.clicked.connect(self.launchCredentials)
        self.ui.userCreatorLaunch.clicked.connect(self.launchUserCreator)
        self.ui.equipmentLaunch.clicked.connect(self.launchEquipment)
        self.ui.update.clicked.connect(self.launchUpdate)
        self.ui.launchEquipmentRegistration.clicked.connect(self.launchEquipmentRegistration)
        self.ui.logOut.clicked.connect(exit)
        self.ui.about.clicked.connect(self.launchAbout)


    def launchPatient(self):        #Launch patient activity
        self.patientActivity=patientActivity(self.credentials)
        self.dialog=dialogActivity("Las fechas se sacan de las listas de control de calidad", onCloseFunc=self.patientActivity.show)

    def launchExport(self):         #Launch export activity
        self.exploitActivity=exploitActivity(self.credentials)
        self.exploitActivity.show()
    
    def launchCredentials(self):    #Launch credentials change activity
        self.credentials=credentialsActivity(self.credentials)
        self.credentials.show()
    
    def launchUserCreator(self):    #Launch user creator activity
        self.userCreator=userCreatorActivity(self.credentials)
        self.userCreator.show()
    
    def launchEquipment(self):      #Launch equipment control activity
        self.equipmentFollow=equipmentActivity(self.credentials)
        self.equipmentFollow.show()

    def launchEquipmentRegistration(self):  #Launch equipment registration activity
        self.equipmentRegistration=equipmentRegistrationActivity(self.credentials)
        self.equipmentRegistration.show()

    def launchAbout(self):          #Launch about activity
        self.about=aboutActivity()
        self.about.show()

    def launchUpdate(self):
        if self.updatable==0:
            if(getVersionInt(getLatestVersion())>getVersionInt(self.conf.version)):
                self.updatable=1
                self.ui.update.setText("Descargar actualización")
            else:
                self.ui.update.setText("No hay actaulizaciones")
                self.ui.update.setEnabled(False)
        elif self.updatable==1:
            self.dialog=dialogActivity("La actualización se descargará en segundo plano, no cierre el programa", 
                buttonMessage="Descargar", 
                onCloseFunc=self.download)
            self.ui.update.setEnabled(False)
            self.ui.update.setText("Descargado")
        
    def download(self):
        if "suite.py" in listdir():
            update("source")
        else:
            update("compiled")
