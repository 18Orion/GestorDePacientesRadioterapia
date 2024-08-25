# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'launcherUI.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_launcher(object):
    def setupUi(self, launcher):
        if not launcher.objectName():
            launcher.setObjectName(u"launcher")
        launcher.resize(672, 639)
        self.formLayoutWidget = QWidget(launcher)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.name = QLabel(self.formLayoutWidget)
        self.name.setObjectName(u"name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.name)

        self.patientUILaunch = QPushButton(self.formLayoutWidget)
        self.patientUILaunch.setObjectName(u"patientUILaunch")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.patientUILaunch)

        self.exportUILaunch = QPushButton(self.formLayoutWidget)
        self.exportUILaunch.setObjectName(u"exportUILaunch")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.exportUILaunch)

        self.importUILaunch = QPushButton(self.formLayoutWidget)
        self.importUILaunch.setObjectName(u"importUILaunch")
        self.importUILaunch.setEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.importUILaunch)

        self.changeCredentialsUILaunch = QPushButton(self.formLayoutWidget)
        self.changeCredentialsUILaunch.setObjectName(u"changeCredentialsUILaunch")
        self.changeCredentialsUILaunch.setEnabled(True)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.changeCredentialsUILaunch)

        self.juntaAnd = QLabel(self.formLayoutWidget)
        self.juntaAnd.setObjectName(u"juntaAnd")
        sizePolicy1.setHeightForWidth(self.juntaAnd.sizePolicy().hasHeightForWidth())
        self.juntaAnd.setSizePolicy(sizePolicy1)
        self.juntaAnd.setMaximumSize(QSize(150, 150))
        self.juntaAnd.setFrameShape(QFrame.Box)
        self.juntaAnd.setText(u"")
        self.juntaAnd.setPixmap(QPixmap(u"../assets/logo.jpg"))
        self.juntaAnd.setScaledContents(True)
        self.juntaAnd.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.juntaAnd)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.label_5)

        self.version = QLabel(self.formLayoutWidget)
        self.version.setObjectName(u"version")

        self.horizontalLayout.addWidget(self.version)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout)

        launcher.setCentralWidget(self.formLayoutWidget)
        self.statusbar = QStatusBar(launcher)
        self.statusbar.setObjectName(u"statusbar")
        launcher.setStatusBar(self.statusbar)

        self.retranslateUi(launcher)

        QMetaObject.connectSlotsByName(launcher)
    # setupUi

    def retranslateUi(self, launcher):
        launcher.setWindowTitle(QCoreApplication.translate("launcher", u"launcher", None))
        self.label.setText(QCoreApplication.translate("launcher", u"Has iniciado sesi\u00f3n como:", None))
        self.name.setText(QCoreApplication.translate("launcher", u"user", None))
        self.patientUILaunch.setText(QCoreApplication.translate("launcher", u"Introducir/Editar tratamiento", None))
        self.exportUILaunch.setText(QCoreApplication.translate("launcher", u"Exportar datos", None))
        self.importUILaunch.setText(QCoreApplication.translate("launcher", u"Importar datos", None))
        self.changeCredentialsUILaunch.setText(QCoreApplication.translate("launcher", u"Cambiar credenciales", None))
        self.label_3.setText(QCoreApplication.translate("launcher", u"Creado por Sergio Mi\u00f1ano Ramos", None))
        self.label_2.setText(QCoreApplication.translate("launcher", u"Servicio de radiof\u00edsica, hospital Reina Sof\u00eda", None))
        self.label_5.setText(QCoreApplication.translate("launcher", u"Versi\u00f3n:", None))
        self.version.setText("")
    # retranslateUi

