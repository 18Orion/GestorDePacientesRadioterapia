# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patientUI.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QComboBox,
    QDateEdit, QDialogButtonBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1496, 790)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QWidget(MainWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 1471, 661))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.layoutWidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setLineWidth(5)
        self.historyLayout = QHBoxLayout(self.frame)
        self.historyLayout.setObjectName(u"historyLayout")
        self.historyLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.historyLayout.addWidget(self.label)

        self.historyNumberEdit = QLineEdit(self.frame)
        self.historyNumberEdit.setObjectName(u"historyNumberEdit")
        self.historyNumberEdit.setMaxLength(10)

        self.historyLayout.addWidget(self.historyNumberEdit)


        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.personalDataFame = QFrame(self.layoutWidget)
        self.personalDataFame.setObjectName(u"personalDataFame")
        self.personalDataFame.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.personalDataFame.sizePolicy().hasHeightForWidth())
        self.personalDataFame.setSizePolicy(sizePolicy2)
        self.personalDataFame.setSizeIncrement(QSize(1, 1))
        self.personalDataLayout = QVBoxLayout(self.personalDataFame)
        self.personalDataLayout.setObjectName(u"personalDataLayout")
        self.personalDataLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.personalDataLayout.setContentsMargins(0, 0, 0, 0)
        self.nameLayout = QHBoxLayout()
        self.nameLayout.setObjectName(u"nameLayout")
        self.label_2 = QLabel(self.personalDataFame)
        self.label_2.setObjectName(u"label_2")

        self.nameLayout.addWidget(self.label_2)

        self.nameEdit = QLineEdit(self.personalDataFame)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setMaxLength(50)
        self.nameEdit.setFrame(True)

        self.nameLayout.addWidget(self.nameEdit)


        self.personalDataLayout.addLayout(self.nameLayout)

        self.surnamesLayout = QHBoxLayout()
        self.surnamesLayout.setObjectName(u"surnamesLayout")
        self.label_5 = QLabel(self.personalDataFame)
        self.label_5.setObjectName(u"label_5")

        self.surnamesLayout.addWidget(self.label_5)

        self.firstSurnameEdit = QLineEdit(self.personalDataFame)
        self.firstSurnameEdit.setObjectName(u"firstSurnameEdit")
        self.firstSurnameEdit.setMaxLength(50)

        self.surnamesLayout.addWidget(self.firstSurnameEdit)

        self.label_4 = QLabel(self.personalDataFame)
        self.label_4.setObjectName(u"label_4")

        self.surnamesLayout.addWidget(self.label_4)

        self.secondSurnameEdit = QLineEdit(self.personalDataFame)
        self.secondSurnameEdit.setObjectName(u"secondSurnameEdit")
        self.secondSurnameEdit.setMaxLength(50)

        self.surnamesLayout.addWidget(self.secondSurnameEdit)


        self.personalDataLayout.addLayout(self.surnamesLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_12 = QLabel(self.personalDataFame)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_3.addWidget(self.label_12)

        self.birthdayEdit = QDateEdit(self.personalDataFame)
        self.birthdayEdit.setObjectName(u"birthdayEdit")
        self.birthdayEdit.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.birthdayEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_13 = QLabel(self.personalDataFame)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_3.addWidget(self.label_13)

        self.genderComboBox = QComboBox(self.personalDataFame)
        self.genderComboBox.setObjectName(u"genderComboBox")

        self.horizontalLayout_3.addWidget(self.genderComboBox)


        self.personalDataLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.personalDataFame)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.treatmentNumber = QComboBox(self.layoutWidget)
        self.treatmentNumber.setObjectName(u"treatmentNumber")

        self.verticalLayout.addWidget(self.treatmentNumber)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(125, 16777215))

        self.horizontalLayout.addWidget(self.label_11)

        self.treatmentOptions = QComboBox(self.layoutWidget)
        self.treatmentOptions.setObjectName(u"treatmentOptions")

        self.horizontalLayout.addWidget(self.treatmentOptions)

        self.horizontalSpacer_2 = QSpacerItem(40, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.calcRetries = QLineEdit(self.layoutWidget)
        self.calcRetries.setObjectName(u"calcRetries")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.calcRetries.sizePolicy().hasHeightForWidth())
        self.calcRetries.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.calcRetries)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_5 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)

        self.technicianComboBox = QComboBox(self.layoutWidget)
        self.technicianComboBox.setObjectName(u"technicianComboBox")
        sizePolicy1.setHeightForWidth(self.technicianComboBox.sizePolicy().hasHeightForWidth())
        self.technicianComboBox.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.technicianComboBox, 1, 1, 1, 1)

        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")
        sizePolicy4.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)

        self.doctorComboBox = QComboBox(self.layoutWidget)
        self.doctorComboBox.setObjectName(u"doctorComboBox")
        sizePolicy1.setHeightForWidth(self.doctorComboBox.sizePolicy().hasHeightForWidth())
        self.doctorComboBox.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.doctorComboBox, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.dateLayout = QHBoxLayout()
        self.dateLayout.setSpacing(6)
        self.dateLayout.setObjectName(u"dateLayout")
        self.dateLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.keyDateEdit = QDateEdit(self.layoutWidget)
        self.keyDateEdit.setObjectName(u"keyDateEdit")
        sizePolicy2.setHeightForWidth(self.keyDateEdit.sizePolicy().hasHeightForWidth())
        self.keyDateEdit.setSizePolicy(sizePolicy2)
        self.keyDateEdit.setCalendarPopup(True)

        self.dateLayout.addWidget(self.keyDateEdit)

        self.dateType = QComboBox(self.layoutWidget)
        self.dateType.setObjectName(u"dateType")
        sizePolicy4.setHeightForWidth(self.dateType.sizePolicy().hasHeightForWidth())
        self.dateType.setSizePolicy(sizePolicy4)

        self.dateLayout.addWidget(self.dateType)

        self.autofillDate = QPushButton(self.layoutWidget)
        self.autofillDate.setObjectName(u"autofillDate")
        sizePolicy3.setHeightForWidth(self.autofillDate.sizePolicy().hasHeightForWidth())
        self.autofillDate.setSizePolicy(sizePolicy3)

        self.dateLayout.addWidget(self.autofillDate)

        self.addDate = QPushButton(self.layoutWidget)
        self.addDate.setObjectName(u"addDate")
        sizePolicy3.setHeightForWidth(self.addDate.sizePolicy().hasHeightForWidth())
        self.addDate.setSizePolicy(sizePolicy3)

        self.dateLayout.addWidget(self.addDate)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.dateLayout.addItem(self.horizontalSpacer_3)

        self.removeDate = QPushButton(self.layoutWidget)
        self.removeDate.setObjectName(u"removeDate")

        self.dateLayout.addWidget(self.removeDate)


        self.verticalLayout.addLayout(self.dateLayout)

        self.dateTableView = QTableWidget(self.layoutWidget)
        if (self.dateTableView.columnCount() < 3):
            self.dateTableView.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.dateTableView.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.dateTableView.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.dateTableView.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.dateTableView.setObjectName(u"dateTableView")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.dateTableView.sizePolicy().hasHeightForWidth())
        self.dateTableView.setSizePolicy(sizePolicy5)
        self.dateTableView.setMaximumSize(QSize(16777215, 600))
        self.dateTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.dateTableView.setTabKeyNavigation(False)
        self.dateTableView.setProperty("showDropIndicator", False)
        self.dateTableView.setDragDropOverwriteMode(False)
        self.dateTableView.horizontalHeader().setMinimumSectionSize(200)
        self.dateTableView.horizontalHeader().setProperty("showSortIndicator", False)
        self.dateTableView.horizontalHeader().setStretchLastSection(True)
        self.dateTableView.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.dateTableView)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.doctorObservationsEdit = QTextEdit(self.tab_2)
        self.doctorObservationsEdit.setObjectName(u"doctorObservationsEdit")
        self.doctorObservationsEdit.setGeometry(QRect(0, 0, 1491, 701))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.physicianObservationsEdit = QTextEdit(self.tab_3)
        self.physicianObservationsEdit.setObjectName(u"physicianObservationsEdit")
        self.physicianObservationsEdit.setGeometry(QRect(0, 0, 1491, 701))
        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.feedBackLabel = QLabel(self.verticalLayoutWidget)
        self.feedBackLabel.setObjectName(u"feedBackLabel")
        sizePolicy1.setHeightForWidth(self.feedBackLabel.sizePolicy().hasHeightForWidth())
        self.feedBackLabel.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setBold(False)
        self.feedBackLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.feedBackLabel)

        self.finalButtons = QDialogButtonBox(self.verticalLayoutWidget)
        self.finalButtons.setObjectName(u"finalButtons")
        self.finalButtons.setStandardButtons(QDialogButtonBox.Reset|QDialogButtonBox.Save)

        self.verticalLayout_2.addWidget(self.finalButtons)

        MainWindow.setCentralWidget(self.verticalLayoutWidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.genderComboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ficha de paciente", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de historial cl\u00ednico (AN): ", None))
        self.historyNumberEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"XXXXXXXXXX", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Primer apellido:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Segundo apellido:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Fecha de nacimiento: ", None))
        self.birthdayEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd-MM-yyyy", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Sexo:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Tipo de tratamiento:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de c\u00e1lculos", None))
        self.calcRetries.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Radiof\u00edsico a cargo:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Doctor a cargo:", None))
        self.keyDateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd-MM-yyyy", None))
        self.autofillDate.setText(QCoreApplication.translate("MainWindow", u"Autocompletar con fecha de hoy", None))
        self.addDate.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Fecha", None))
        self.removeDate.setText(QCoreApplication.translate("MainWindow", u"Borrar \u00faltima fecha", None))
        ___qtablewidgetitem = self.dateTableView.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Tipo de fecha", None));
        ___qtablewidgetitem1 = self.dateTableView.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem2 = self.dateTableView.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"D\u00edas desde la recepci\u00f3n", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Datos del paciente", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Observaciones del m\u00e9dico", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Observaciones del radiof\u00edsico", None))
        self.feedBackLabel.setText("")
    # retranslateUi

