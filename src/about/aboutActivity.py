# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow
from src.about.aboutUI import Ui_aboutActivity
from libs.confReader import confReader

class aboutActivity(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_aboutActivity()
        self.ui.setupUi(self)
        conf=confReader()
        self.ui.python.setText(conf.pythonVersion)
        self.ui.MySQL.setText(conf.mysql)
        self.ui.version.setText(conf.version)