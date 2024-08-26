# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userCreatorUI.ui'
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
    QWidget)

class Ui_userCreatorActivity(object):
    def setupUi(self, userCreatorActivity):
        if not userCreatorActivity.objectName():
            userCreatorActivity.setObjectName(u"userCreatorActivity")
        userCreatorActivity.resize(800, 600)
        self.formLayoutWidget = QWidget(userCreatorActivity)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_4)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.user = QLineEdit(self.formLayoutWidget)
        self.user.setObjectName(u"user")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.user)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.formLayout.setItem(2, QFormLayout.SpanningRole, self.verticalSpacer)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.password = QLineEdit(self.formLayoutWidget)
        self.password.setObjectName(u"password")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.password)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.repeatPassword = QLineEdit(self.formLayoutWidget)
        self.repeatPassword.setObjectName(u"repeatPassword")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.repeatPassword)

        self.createUser = QPushButton(self.formLayoutWidget)
        self.createUser.setObjectName(u"createUser")

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.createUser)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.label_5)

        userCreatorActivity.setCentralWidget(self.formLayoutWidget)

        self.retranslateUi(userCreatorActivity)

        QMetaObject.connectSlotsByName(userCreatorActivity)
    # setupUi

    def retranslateUi(self, userCreatorActivity):
        userCreatorActivity.setWindowTitle(QCoreApplication.translate("userCreatorActivity", u"userCreatorActivity", None))
        self.label_4.setText(QCoreApplication.translate("userCreatorActivity", u"Introiduzca las credenciales de usuario", None))
        self.label.setText(QCoreApplication.translate("userCreatorActivity", u"Usuario", None))
        self.label_2.setText(QCoreApplication.translate("userCreatorActivity", u"Contrase\u00f1a", None))
        self.label_3.setText(QCoreApplication.translate("userCreatorActivity", u"Contrase\u00f1a", None))
        self.createUser.setText(QCoreApplication.translate("userCreatorActivity", u"Crear usuario", None))
        self.label_5.setText(QCoreApplication.translate("userCreatorActivity", u"Las credenciales deben estar escritas en min\u00fasculas y sin espacios ni car\u00e1cteres especiales", None))
    # retranslateUi

