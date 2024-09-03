# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutUI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QMainWindow,
    QSizePolicy, QWidget)

class Ui_aboutActivity(object):
    def setupUi(self, aboutActivity):
        if not aboutActivity.objectName():
            aboutActivity.setObjectName(u"aboutActivity")
        aboutActivity.resize(517, 101)
        self.centralwidget = QWidget(aboutActivity)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.version = QLabel(self.centralwidget)
        self.version.setObjectName(u"version")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.version)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.python = QLabel(self.centralwidget)
        self.python.setObjectName(u"python")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.python)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.MySQL = QLabel(self.centralwidget)
        self.MySQL.setObjectName(u"MySQL")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.MySQL)

        aboutActivity.setCentralWidget(self.centralwidget)

        self.retranslateUi(aboutActivity)

        QMetaObject.connectSlotsByName(aboutActivity)
    # setupUi

    def retranslateUi(self, aboutActivity):
        aboutActivity.setWindowTitle(QCoreApplication.translate("aboutActivity", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("aboutActivity", u"Versi\u00f3n:", None))
        self.version.setText("")
        self.label_3.setText(QCoreApplication.translate("aboutActivity", u"Versi\u00f3n de Python", None))
        self.python.setText("")
        self.label_5.setText(QCoreApplication.translate("aboutActivity", u"Versi\u00f3n de MySQL:", None))
        self.MySQL.setText("")
    # retranslateUi

