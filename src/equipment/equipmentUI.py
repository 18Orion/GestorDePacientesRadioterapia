# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'equipmentUI.ui'
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
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_equipmentActivity(object):
    def setupUi(self, equipmentActivity):
        if not equipmentActivity.objectName():
            equipmentActivity.setObjectName(u"equipmentActivity")
        equipmentActivity.resize(880, 558)
        self.verticalLayoutWidget = QWidget(equipmentActivity)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.brandComboBox = QComboBox(self.verticalLayoutWidget)
        self.brandComboBox.setObjectName(u"brandComboBox")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.brandComboBox)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.modelComboBox = QComboBox(self.verticalLayoutWidget)
        self.modelComboBox.setObjectName(u"modelComboBox")
        self.modelComboBox.setEnabled(False)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.modelComboBox)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.serialNumberComboBox = QComboBox(self.verticalLayoutWidget)
        self.serialNumberComboBox.setObjectName(u"serialNumberComboBox")
        self.serialNumberComboBox.setEnabled(False)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.serialNumberComboBox)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.comment = QLabel(self.verticalLayoutWidget)
        self.comment.setObjectName(u"comment")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.comment)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.formLayout_2.setItem(4, QFormLayout.SpanningRole, self.verticalSpacer)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_6)

        self.radiophysicianComboBox = QComboBox(self.verticalLayoutWidget)
        self.radiophysicianComboBox.setObjectName(u"radiophysicianComboBox")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.radiophysicianComboBox)

        self.technicianComboBox = QComboBox(self.verticalLayoutWidget)
        self.technicianComboBox.setObjectName(u"technicianComboBox")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.technicianComboBox)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame)

        equipmentActivity.setCentralWidget(self.verticalLayoutWidget)

        self.retranslateUi(equipmentActivity)

        QMetaObject.connectSlotsByName(equipmentActivity)
    # setupUi

    def retranslateUi(self, equipmentActivity):
        equipmentActivity.setWindowTitle(QCoreApplication.translate("equipmentActivity", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("equipmentActivity", u"Marca:", None))
        self.label_2.setText(QCoreApplication.translate("equipmentActivity", u"Modelo:", None))
        self.label_3.setText(QCoreApplication.translate("equipmentActivity", u"N\u00famero de serie", None))
        self.label_4.setText(QCoreApplication.translate("equipmentActivity", u"Comentario:", None))
        self.comment.setText("")
        self.label_5.setText(QCoreApplication.translate("equipmentActivity", u"Radiof\u00edsico", None))
        self.label_6.setText(QCoreApplication.translate("equipmentActivity", u"T\u00e9cnico:", None))
        self.pushButton.setText(QCoreApplication.translate("equipmentActivity", u"PushButton", None))
    # retranslateUi

