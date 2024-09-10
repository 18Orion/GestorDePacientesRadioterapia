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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QDateEdit, QFormLayout, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_equipmentActivity(object):
    def setupUi(self, equipmentActivity):
        if not equipmentActivity.objectName():
            equipmentActivity.setObjectName(u"equipmentActivity")
        equipmentActivity.resize(932, 645)
        self.verticalLayoutWidget = QWidget(equipmentActivity)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.centreComboBox = QComboBox(self.verticalLayoutWidget)
        self.centreComboBox.setObjectName(u"centreComboBox")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.centreComboBox)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.serviceComboBox = QComboBox(self.verticalLayoutWidget)
        self.serviceComboBox.setObjectName(u"serviceComboBox")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.serviceComboBox)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.locationComboBox = QComboBox(self.verticalLayoutWidget)
        self.locationComboBox.setObjectName(u"locationComboBox")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.locationComboBox)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.formLayout_2.setItem(6, QFormLayout.SpanningRole, self.verticalSpacer)

        self.tabWidget = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.filling = QWidget()
        self.filling.setObjectName(u"filling")
        self.verticalLayout_2 = QVBoxLayout(self.filling)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.filling)
        self.label_7.setObjectName(u"label_7")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_7)

        self.operation = QComboBox(self.filling)
        self.operation.setObjectName(u"operation")
        self.operation.setEnabled(False)

        self.horizontalLayout.addWidget(self.operation)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.data = QFrame(self.filling)
        self.data.setObjectName(u"data")
        self.data.setEnabled(False)
        self.data.setFrameShape(QFrame.NoFrame)
        self.formLayout = QFormLayout(self.data)
        self.formLayout.setObjectName(u"formLayout")
        self.radiophysicianComboBox = QComboBox(self.data)
        self.radiophysicianComboBox.setObjectName(u"radiophysicianComboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.radiophysicianComboBox)

        self.label_5 = QLabel(self.data)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.data)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.technicianComboBox = QComboBox(self.data)
        self.technicianComboBox.setObjectName(u"technicianComboBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.technicianComboBox)

        self.label_8 = QLabel(self.data)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.data)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_9)

        self.label_10 = QLabel(self.data)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_10)

        self.beginDate = QDateEdit(self.data)
        self.beginDate.setObjectName(u"beginDate")
        self.beginDate.setCalendarPopup(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.beginDate)

        self.endDate = QDateEdit(self.data)
        self.endDate.setObjectName(u"endDate")
        self.endDate.setCalendarPopup(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.endDate)

        self.typeOfOperation = QComboBox(self.data)
        self.typeOfOperation.setObjectName(u"typeOfOperation")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.typeOfOperation)


        self.verticalLayout_2.addWidget(self.data)

        self.save = QPushButton(self.filling)
        self.save.setObjectName(u"save")

        self.verticalLayout_2.addWidget(self.save)

        self.tabWidget.addTab(self.filling, "")
        self.history = QWidget()
        self.history.setObjectName(u"history")
        self.verticalLayout_3 = QVBoxLayout(self.history)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.historyTable = QTableWidget(self.history)
        if (self.historyTable.columnCount() < 6):
            self.historyTable.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.historyTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.historyTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.historyTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.historyTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.historyTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.historyTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.historyTable.setObjectName(u"historyTable")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.historyTable.sizePolicy().hasHeightForWidth())
        self.historyTable.setSizePolicy(sizePolicy1)
        self.historyTable.setFrameShape(QFrame.NoFrame)
        self.historyTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.historyTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.historyTable.horizontalHeader().setCascadingSectionResizes(False)
        self.historyTable.horizontalHeader().setMinimumSectionSize(60)
        self.historyTable.horizontalHeader().setDefaultSectionSize(140)
        self.historyTable.horizontalHeader().setStretchLastSection(True)
        self.historyTable.verticalHeader().setVisible(False)
        self.historyTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_3.addWidget(self.historyTable)

        self.tabWidget.addTab(self.history, "")

        self.formLayout_2.setWidget(7, QFormLayout.SpanningRole, self.tabWidget)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_11)

        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_12)

        self.brandComboBox = QComboBox(self.verticalLayoutWidget)
        self.brandComboBox.setObjectName(u"brandComboBox")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.brandComboBox)

        self.serialComboBox = QComboBox(self.verticalLayoutWidget)
        self.serialComboBox.setObjectName(u"serialComboBox")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.serialComboBox)

        self.modelComboBox = QComboBox(self.verticalLayoutWidget)
        self.modelComboBox.setObjectName(u"modelComboBox")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.modelComboBox)


        self.verticalLayout.addLayout(self.formLayout_2)

        equipmentActivity.setCentralWidget(self.verticalLayoutWidget)

        self.retranslateUi(equipmentActivity)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(equipmentActivity)
    # setupUi

    def retranslateUi(self, equipmentActivity):
        equipmentActivity.setWindowTitle(QCoreApplication.translate("equipmentActivity", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("equipmentActivity", u"Centro:", None))
        self.label_2.setText(QCoreApplication.translate("equipmentActivity", u"Servicio:", None))
        self.label_3.setText(QCoreApplication.translate("equipmentActivity", u"Ubicaci\u00f3n:", None))
        self.label_7.setText(QCoreApplication.translate("equipmentActivity", u"Operaci\u00f3n", None))
        self.label_5.setText(QCoreApplication.translate("equipmentActivity", u"Radiof\u00edsico", None))
        self.label_6.setText(QCoreApplication.translate("equipmentActivity", u"T\u00e9cnico:", None))
        self.label_8.setText(QCoreApplication.translate("equipmentActivity", u"Tipo de operaci\u00f3n", None))
        self.label_9.setText(QCoreApplication.translate("equipmentActivity", u"Fecha de inicio", None))
        self.label_10.setText(QCoreApplication.translate("equipmentActivity", u"Fecha de fin:", None))
        self.beginDate.setDisplayFormat(QCoreApplication.translate("equipmentActivity", u"dd/MM/yyyy", None))
        self.endDate.setDisplayFormat(QCoreApplication.translate("equipmentActivity", u"dd/MM/yyyy", None))
        self.save.setText(QCoreApplication.translate("equipmentActivity", u"Guardar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.filling), QCoreApplication.translate("equipmentActivity", u"Edici\u00f3n de operaciones", None))
        ___qtablewidgetitem = self.historyTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("equipmentActivity", u"N\u00famero de operaci\u00f3n", None));
        ___qtablewidgetitem1 = self.historyTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("equipmentActivity", u"Tipo de operaci\u00f3n", None));
        ___qtablewidgetitem2 = self.historyTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("equipmentActivity", u"Radiof\u00edsico", None));
        ___qtablewidgetitem3 = self.historyTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("equipmentActivity", u"T\u00e9cnico", None));
        ___qtablewidgetitem4 = self.historyTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("equipmentActivity", u"Fecha de inicio", None));
        ___qtablewidgetitem5 = self.historyTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("equipmentActivity", u"Fecha de final", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.history), QCoreApplication.translate("equipmentActivity", u"Historial", None))
        self.label_4.setText(QCoreApplication.translate("equipmentActivity", u"Marca:", None))
        self.label_11.setText(QCoreApplication.translate("equipmentActivity", u"Modelo:", None))
        self.label_12.setText(QCoreApplication.translate("equipmentActivity", u"N\u00famero de serie:", None))
    # retranslateUi

