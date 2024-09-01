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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QLabel,
    QLayout, QMainWindow, QSizePolicy, QVBoxLayout,
    QWidget)

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

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.comment = QLabel(self.verticalLayoutWidget)
        self.comment.setObjectName(u"comment")

        self.formLayout_2.setWidget(3, QFormLayout.SpanningRole, self.comment)

        self.brandComboBox = QComboBox(self.verticalLayoutWidget)
        self.brandComboBox.setObjectName(u"brandComboBox")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.brandComboBox)

        self.modelComboBox = QComboBox(self.verticalLayoutWidget)
        self.modelComboBox.setObjectName(u"modelComboBox")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.modelComboBox)

        self.serialNumberComboBox = QComboBox(self.verticalLayoutWidget)
        self.serialNumberComboBox.setObjectName(u"serialNumberComboBox")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.serialNumberComboBox)


        self.verticalLayout.addLayout(self.formLayout_2)

        equipmentActivity.setCentralWidget(self.verticalLayoutWidget)

        self.retranslateUi(equipmentActivity)

        QMetaObject.connectSlotsByName(equipmentActivity)
    # setupUi

    def retranslateUi(self, equipmentActivity):
        equipmentActivity.setWindowTitle(QCoreApplication.translate("equipmentActivity", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("equipmentActivity", u"Marca:", None))
        self.label_2.setText(QCoreApplication.translate("equipmentActivity", u"Modelo:", None))
        self.label_3.setText(QCoreApplication.translate("equipmentActivity", u"N\u00famero de serie", None))
        self.comment.setText(QCoreApplication.translate("equipmentActivity", u"Comentario:", None))
    # retranslateUi

