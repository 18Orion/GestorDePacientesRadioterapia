# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogUI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(586, 139)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.advise = QLabel(Dialog)
        self.advise.setObjectName(u"advise")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.advise.sizePolicy().hasHeightForWidth())
        self.advise.setSizePolicy(sizePolicy)
        self.advise.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.advise)

        self.okButton = QPushButton(Dialog)
        self.okButton.setObjectName(u"okButton")

        self.verticalLayout_2.addWidget(self.okButton)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Di\u00e1logo", None))
        self.advise.setText("")
        self.okButton.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
    # retranslateUi

