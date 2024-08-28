# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'credentialsUI.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Credentials(object):
    def setupUi(self, Credentials):
        if not Credentials.objectName():
            Credentials.setObjectName(u"Credentials")
        Credentials.resize(800, 204)
        self.verticalLayoutWidget = QWidget(Credentials)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.user = QLineEdit(self.verticalLayoutWidget)
        self.user.setObjectName(u"user")
        self.user.setEnabled(False)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.user)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.oldPassword = QLineEdit(self.verticalLayoutWidget)
        self.oldPassword.setObjectName(u"oldPassword")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.oldPassword)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_2.setItem(2, QFormLayout.SpanningRole, self.verticalSpacer)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.newPassword = QLineEdit(self.verticalLayoutWidget)
        self.newPassword.setObjectName(u"newPassword")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.newPassword)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.confPassword = QLineEdit(self.verticalLayoutWidget)
        self.confPassword.setObjectName(u"confPassword")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.confPassword)

        self.changePassword = QPushButton(self.verticalLayoutWidget)
        self.changePassword.setObjectName(u"changePassword")

        self.formLayout_2.setWidget(6, QFormLayout.SpanningRole, self.changePassword)

        self.feedback = QLabel(self.verticalLayoutWidget)
        self.feedback.setObjectName(u"feedback")

        self.formLayout_2.setWidget(5, QFormLayout.SpanningRole, self.feedback)


        self.verticalLayout.addLayout(self.formLayout_2)

        Credentials.setCentralWidget(self.verticalLayoutWidget)

        self.retranslateUi(Credentials)

        QMetaObject.connectSlotsByName(Credentials)
    # setupUi

    def retranslateUi(self, Credentials):
        Credentials.setWindowTitle(QCoreApplication.translate("Credentials", u"Cambio de contrase\u00f1a", None))
        self.label_5.setText(QCoreApplication.translate("Credentials", u"La aplicaci\u00f3n se cerrara al cambiar la contrase\u00f1a", None))
        self.label.setText(QCoreApplication.translate("Credentials", u"Usuario:", None))
        self.label_2.setText(QCoreApplication.translate("Credentials", u"Contrase\u00f1a:", None))
        self.label_3.setText(QCoreApplication.translate("Credentials", u"Nueva contras\u00f1a:", None))
        self.label_4.setText(QCoreApplication.translate("Credentials", u"Confirmar contrase\u00f1a:", None))
        self.changePassword.setText(QCoreApplication.translate("Credentials", u"Cambiar contrase\u00f1a", None))
        self.feedback.setText("")
    # retranslateUi

