# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'equipmentRegistrationUI.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_equipmentRegistrationActivity(object):
    def setupUi(self, equipmentRegistrationActivity):
        if not equipmentRegistrationActivity.objectName():
            equipmentRegistrationActivity.setObjectName(u"equipmentRegistrationActivity")
        equipmentRegistrationActivity.resize(880, 585)
        self.verticalLayoutWidget = QWidget(equipmentRegistrationActivity)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        font = QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)

        self.verticalLayout.addWidget(self.label_12)

        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.locationEdit = QLineEdit(self.frame)
        self.locationEdit.setObjectName(u"locationEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.locationEdit)

        self.centreComboBox = QComboBox(self.frame)
        self.centreComboBox.setObjectName(u"centreComboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.centreComboBox)

        self.serviceComboBox = QComboBox(self.frame)
        self.serviceComboBox.setObjectName(u"serviceComboBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.serviceComboBox)


        self.verticalLayout.addWidget(self.frame)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.frame_2 = QFrame(self.verticalLayoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.formLayout_3 = QFormLayout(self.frame_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.serialNumberEdit = QLineEdit(self.frame_2)
        self.serialNumberEdit.setObjectName(u"serialNumberEdit")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.serialNumberEdit)

        self.brandComboBox = QComboBox(self.frame_2)
        self.brandComboBox.setObjectName(u"brandComboBox")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.brandComboBox)

        self.modelLineEdit = QLineEdit(self.frame_2)
        self.modelLineEdit.setObjectName(u"modelLineEdit")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.modelLineEdit)


        self.verticalLayout.addWidget(self.frame_2)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout.addWidget(self.label_8)

        self.frame_3 = QFrame(self.verticalLayoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.formLayout_4 = QFormLayout(self.frame_3)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.generatorBrandComboBox = QComboBox(self.frame_3)
        self.generatorBrandComboBox.setObjectName(u"generatorBrandComboBox")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.generatorBrandComboBox)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_10)

        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_11)

        self.generatorSerialNumberEdit = QLineEdit(self.frame_3)
        self.generatorSerialNumberEdit.setObjectName(u"generatorSerialNumberEdit")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.generatorSerialNumberEdit)

        self.generatorModelLineEdit = QLineEdit(self.frame_3)
        self.generatorModelLineEdit.setObjectName(u"generatorModelLineEdit")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.generatorModelLineEdit)


        self.verticalLayout.addWidget(self.frame_3)

        self.registrateEquipment = QPushButton(self.verticalLayoutWidget)
        self.registrateEquipment.setObjectName(u"registrateEquipment")

        self.verticalLayout.addWidget(self.registrateEquipment)

        equipmentRegistrationActivity.setCentralWidget(self.verticalLayoutWidget)

        self.retranslateUi(equipmentRegistrationActivity)

        QMetaObject.connectSlotsByName(equipmentRegistrationActivity)
    # setupUi

    def retranslateUi(self, equipmentRegistrationActivity):
        equipmentRegistrationActivity.setWindowTitle(QCoreApplication.translate("equipmentRegistrationActivity", u"MainWindow", None))
        self.label_12.setText(QCoreApplication.translate("equipmentRegistrationActivity", u"Ubicaci\u00f3n del equipo", None))
        self.label_6.setText(QCoreApplication.translate("equipmentRegistrationActivity", u"Centro:", None))
        self.label_7.setText(QCoreApplication.translate("equipmentRegistrationActivity", u"Servicio:", None))
        self.label_4.setText(QCoreApplication.translate("equipmentRegistrationActivity", u"Ubicaci\u00f3n:", None))
        self.label_5.setText(QCoreApplication.translate("equipmentRegistrationActivity", u"Datos t\u00e9cnicos del equipo", None))
        self.label.setText(QCoreApplication.translate("equipmentRegistrationActivity", u"Marca:", None))
        self.label_2.setText(QCoreApplication.translate("equipmentRegistrationActivity", u"Modelo:", None))
        self.label_3.setText(QCoreApplication.translate("equipmentRegistrationActivity", u"N\u00famero de serie:", None))
        self.label_8.setText(QCoreApplication.translate("equipmentRegistrationActivity", u"Datos del generador", None))
        self.label_9.setText(QCoreApplication.translate("equipmentRegistrationActivity", u"Marca:", None))
        self.label_10.setText(QCoreApplication.translate("equipmentRegistrationActivity", u"Modelo:", None))
        self.label_11.setText(QCoreApplication.translate("equipmentRegistrationActivity", u"Numero de serie", None))
        self.registrateEquipment.setText(QCoreApplication.translate("equipmentRegistrationActivity", u"Registrar equipo", None))
    # retranslateUi

