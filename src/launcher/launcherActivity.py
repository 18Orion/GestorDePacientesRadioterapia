# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from .launcherUI import Ui_launcher

#Import all activities
from src.patient.patientActivity import patientActivity     #Introducing patient data
from src.exploit.exploitActivity import exploitActivity     #Exporting data


class launcherActivity(QMainWindow):
    def __init__(self, credentials, parent=None):
        super().__init__(parent)
        self.ui = Ui_launcher()
        self.ui.setupUi(self)
        self.ui.name.setText(credentials[0])
        self.credentials=credentials
        self.ui.patientUILaunch.clicked.connect(self.launchPatient)
        self.ui.exportUILaunch.clicked.connect(self.launchExport)

    def launchPatient(self):
        self.patientActivity=patientActivity(self.credentials)
        self.patientActivity.show()
        #self.hide()

    def launchExport(self):
        self.exploitActivity=exploitActivity(self.credentials)
        self.exploitActivity.show()
        #self.hide()
