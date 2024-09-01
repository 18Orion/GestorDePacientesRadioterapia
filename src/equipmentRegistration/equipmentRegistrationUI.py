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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_equipmentRegistrationActivity(object):
    def setupUi(self, equipmentRegistrationActivity):
        if not equipmentRegistrationActivity.objectName():
            equipmentRegistrationActivity.setObjectName(u"equipmentRegistrationActivity")
        equipmentRegistrationActivity.resize(880, 196)
        self.verticalLayoutWidget = QWidget(equipmentRegistrationActivity)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.modelEdit = QLineEdit(self.verticalLayoutWidget)
        self.modelEdit.setObjectName(u"modelEdit")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.modelEdit)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.serialNumberEdit = QLineEdit(self.verticalLayoutWidget)
        self.serialNumberEdit.setObjectName(u"serialNumberEdit")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.serialNumberEdit)

        self.brandEdit = QLineEdit(self.verticalLayoutWidget)
        self.brandEdit.setObjectName(u"brandEdit")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.brandEdit)

        self.commentEdit = QLineEdit(self.verticalLayoutWidget)
        self.commentEdit.setObjectName(u"commentEdit")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.commentEdit)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.registrateEquipment = QPushButton(self.verticalLayoutWidget)
        self.registrateEquipment.setObjectName(u"registrateEquipment")

        self.formLayout_2.setWidget(4, QFormLayout.SpanningRole, self.registrateEquipment)


        self.verticalLayout.addLayout(self.formLayout_2)

        equipmentRegistrationActivity.setCentralWidget(self.verticalLayoutWidget)

        self.retranslateUi(equipmentRegistrationActivity)

        QMetaObject.connectSlotsByName(equipmentRegistrationActivity)
    # setupUi

    def retranslateUi(self, equipmentRegistrationActivity):
        equipmentRegistrationActivity.setWindowTitle(QCoreApplication.translate("equipmentRegistrationActivity", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("equipmentRegistrationActivity", u"Marca:", None))
        self.label_2.setText(QCoreApplication.translate("equipmentRegistrationActivity", u"Modelo:", None))
        self.label_3.setText(QCoreApplication.translate("equipmentRegistrationActivity", u"N\u00famero de serie", None))
        self.label_4.setText(QCoreApplication.translate("equipmentRegistrationActivity", u"Comentario:", None))
        self.registrateEquipment.setText(QCoreApplication.translate("equipmentRegistrationActivity", u"Registrar equipo", None))
    # retranslateUi

