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


class launcherActivity(QMainWindow):
    def __init__(self, credentials, parent=None):
        super().__init__(parent)
        self.ui = Ui_launcher()
        self.ui.setupUi(self)
        self.ui.name.setText(credentials[0])
        self.credentials=credentials
        self.ui.patientUILaunch.clicked.connect(self.launchPatient)
        self.ui.exportUILaunch.clicked.connect(self.launchExport)
        self.ui.changeCredentialsUILaunch.clicked.connect(self.launchCredentials)
        self.ui.userCreatorLaunch.clicked.connect(self.launchUserCreator)
        self.ui.equipmentLaunch.clicked.connect(self.launchEquipment)
        self.conf=confReader()
        self.ui.version.setText(self.conf.version)
        self.ui.juntaAnd.setPixmap(QPixmap(u"./assets/logo.jpg"))
        self.ui.userCreatorLaunch.setEnabled(credentials[0]=="root")
        self.ui.update.clicked.connect(self.launchUpdate)
        self.ui.launchEquipmentRegistration.clicked.connect(self.launchEquipmentRegistration)
        self.ui.logOut.clicked.connect(exit)
        self.updatable=0


    def launchPatient(self):
        self.patientActivity=patientActivity(self.credentials)
        self.patientActivity.show()

    def launchExport(self):
        self.exploitActivity=exploitActivity(self.credentials)
        self.exploitActivity.show()
    
    def launchCredentials(self):
        self.credentials=credentialsActivity(self.credentials)
        self.credentials.show()
    
    def launchUserCreator(self):
        self.userCreator=userCreatorActivity(self.credentials)
        self.userCreator.show()
    
    def launchEquipment(self):
        self.equipmentFollow=equipmentActivity(self.credentials)
        self.equipmentFollow.show()

    def launchEquipmentRegistration(self):
        self.equipmentRegistration=equipmentRegistrationActivity(self.credentials)
        self.equipmentRegistration.show()

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
