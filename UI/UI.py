# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1383, 924)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupboxSymptom = QtWidgets.QGroupBox(self.centralwidget)
        self.groupboxSymptom.setGeometry(QtCore.QRect(10, 80, 241, 411))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.groupboxSymptom.setFont(font)
        self.groupboxSymptom.setObjectName("groupboxSymptom")
        self.lineeditSymptom = QtWidgets.QLineEdit(self.groupboxSymptom)
        self.lineeditSymptom.setGeometry(QtCore.QRect(20, 30, 161, 41))
        self.lineeditSymptom.setObjectName("lineeditSymptom")
        self.tablewidgetSymptom = QtWidgets.QTableWidget(self.groupboxSymptom)
        self.tablewidgetSymptom.setGeometry(QtCore.QRect(20, 80, 161, 321))
        self.tablewidgetSymptom.setObjectName("tablewidgetSymptom")
        self.tablewidgetSymptom.setColumnCount(0)
        self.tablewidgetSymptom.setRowCount(0)
        self.buttonSymptom = QtWidgets.QPushButton(self.groupboxSymptom)
        self.buttonSymptom.setGeometry(QtCore.QRect(180, 30, 41, 41))
        self.buttonSymptom.setObjectName("ButtonSymptom")
        self.tablewidgetPrescribe = QtWidgets.QTableWidget(self.centralwidget)
        self.tablewidgetPrescribe.setGeometry(QtCore.QRect(50, 550, 861, 291))
        self.tablewidgetPrescribe.setObjectName("tablewidgetPrescribe")
        self.tablewidgetPrescribe.setColumnCount(0)
        self.tablewidgetPrescribe.setRowCount(0)
        self.buttonInputModel = QtWidgets.QPushButton(self.centralwidget)
        self.buttonInputModel.setGeometry(QtCore.QRect(580, 10, 161, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.buttonInputModel.setFont(font)
        self.buttonInputModel.setObjectName("ButtonInputModel")
        self.tablewidgetBook = QtWidgets.QTableWidget(self.centralwidget)
        self.tablewidgetBook.setGeometry(QtCore.QRect(990, 100, 361, 741))
        self.tablewidgetBook.setObjectName("tablewidgetBook")
        self.tablewidgetBook.setColumnCount(0)
        self.tablewidgetBook.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, -10, 191, 91))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButtonInquiryModel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonInquiryModel.setGeometry(QtCore.QRect(750, 10, 161, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.pushButtonInquiryModel.setFont(font)
        self.pushButtonInquiryModel.setObjectName("pushButtonInquiryModel")
        self.labelPosition = QtWidgets.QLabel(self.centralwidget)
        self.labelPosition.setGeometry(QtCore.QRect(210, -10, 191, 91))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(22)
        self.labelPosition.setFont(font)
        self.labelPosition.setObjectName("labelPosition")
        self.groupboxDisease = QtWidgets.QGroupBox(self.centralwidget)
        self.groupboxDisease.setGeometry(QtCore.QRect(220, 80, 251, 411))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.groupboxDisease.setFont(font)
        self.groupboxDisease.setObjectName("groupboxDisease")
        self.lineDisease = QtWidgets.QLineEdit(self.groupboxDisease)
        self.lineDisease.setGeometry(QtCore.QRect(20, 30, 191, 41))
        self.lineDisease.setObjectName("lineDisease")
        self.tablewidgetDisease = QtWidgets.QTableWidget(self.groupboxDisease)
        self.tablewidgetDisease.setGeometry(QtCore.QRect(20, 80, 191, 321))
        self.tablewidgetDisease.setObjectName("tablewidgetDisease")
        self.tablewidgetDisease.setColumnCount(0)
        self.tablewidgetDisease.setRowCount(0)
        self.buttonDisease = QtWidgets.QPushButton(self.groupboxDisease)
        self.buttonDisease.setGeometry(QtCore.QRect(210, 30, 41, 41))
        self.buttonDisease.setObjectName("ButtonDisease")
        self.groupboxPrescription = QtWidgets.QGroupBox(self.centralwidget)
        self.groupboxPrescription.setGeometry(QtCore.QRect(460, 80, 251, 411))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.groupboxPrescription.setFont(font)
        self.groupboxPrescription.setObjectName("groupboxPrescription")
        self.linePrescription = QtWidgets.QLineEdit(self.groupboxPrescription)
        self.linePrescription.setGeometry(QtCore.QRect(20, 30, 191, 41))
        self.linePrescription.setObjectName("linePrescription")
        self.tablewidgetPrescription = QtWidgets.QTableWidget(self.groupboxPrescription)
        self.tablewidgetPrescription.setGeometry(QtCore.QRect(20, 80, 191, 321))
        self.tablewidgetPrescription.setObjectName("tablewidgetPrescription")
        self.tablewidgetPrescription.setColumnCount(0)
        self.tablewidgetPrescription.setRowCount(0)
        self.buttonPrescription = QtWidgets.QPushButton(self.groupboxPrescription)
        self.buttonPrescription.setGeometry(QtCore.QRect(210, 30, 41, 41))
        self.buttonPrescription.setObjectName("ButtonPrescription")
        self.groupboxMedicine = QtWidgets.QGroupBox(self.centralwidget)
        self.groupboxMedicine.setGeometry(QtCore.QRect(700, 80, 271, 411))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.groupboxMedicine.setFont(font)
        self.groupboxMedicine.setObjectName("groupboxMedicine")
        self.lineMedicine = QtWidgets.QLineEdit(self.groupboxMedicine)
        self.lineMedicine.setGeometry(QtCore.QRect(20, 30, 191, 41))
        self.lineMedicine.setObjectName("lineMedicine")
        self.tablewidgetMedicine = QtWidgets.QTableWidget(self.groupboxMedicine)
        self.tablewidgetMedicine.setGeometry(QtCore.QRect(20, 80, 191, 321))
        self.tablewidgetMedicine.setObjectName("tablewidgetMedicine")
        self.tablewidgetMedicine.setColumnCount(0)
        self.tablewidgetMedicine.setRowCount(0)
        self.buttonMedicine = QtWidgets.QPushButton(self.groupboxMedicine)
        self.buttonMedicine.setGeometry(QtCore.QRect(210, 30, 41, 41))
        self.buttonMedicine.setObjectName("ButtonMedicine")
        self.buttonInitial = QtWidgets.QPushButton(self.centralwidget)
        self.buttonInitial.setGeometry(QtCore.QRect(570, 490, 161, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.buttonInitial.setFont(font)
        self.buttonInitial.setObjectName("ButtonInitial")
        self.buttonInput = QtWidgets.QPushButton(self.centralwidget)
        self.buttonInput.setGeometry(QtCore.QRect(750, 490, 161, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.buttonInput.setFont(font)
        self.buttonInput.setObjectName("ButtonInput")
        self.buttonClean = QtWidgets.QPushButton(self.centralwidget)
        self.buttonClean.setGeometry(QtCore.QRect(570, 850, 161, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.buttonClean.setFont(font)
        self.buttonClean.setObjectName("ButtonClean")
        self.buttonSave = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSave.setGeometry(QtCore.QRect(750, 850, 161, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.buttonSave.setFont(font)
        self.buttonSave.setObjectName("ButtonSave")
        self.lineBook = QtWidgets.QLineEdit(self.centralwidget)
        self.lineBook.setGeometry(QtCore.QRect(1110, 40, 191, 41))
        self.lineBook.setObjectName("lineBook")
        self.labelPosition_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelPosition_2.setGeometry(QtCore.QRect(1000, 10, 191, 91))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(22)
        self.labelPosition_2.setFont(font)
        self.labelPosition_2.setObjectName("labelPosition_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1383, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupboxSymptom.setTitle(_translate("MainWindow", "病症"))
        self.buttonSymptom.setText(_translate("MainWindow", "+"))
        self.buttonInputModel.setText(_translate("MainWindow", "录入模式"))
        self.label.setText(_translate("MainWindow", "当前位置："))
        self.pushButtonInquiryModel.setText(_translate("MainWindow", "问诊模式"))
        self.labelPosition.setText(_translate("MainWindow", "当前位置"))
        self.groupboxDisease.setTitle(_translate("MainWindow", "病名"))
        self.buttonDisease.setText(_translate("MainWindow", "+"))
        self.groupboxPrescription.setTitle(_translate("MainWindow", "药方"))
        self.buttonPrescription.setText(_translate("MainWindow", "+"))
        self.groupboxMedicine.setTitle(_translate("MainWindow", "药"))
        self.buttonMedicine.setText(_translate("MainWindow", "+"))
        self.buttonInitial.setText(_translate("MainWindow", "初始化"))
        self.buttonInput.setText(_translate("MainWindow", "录入"))
        self.buttonClean.setText(_translate("MainWindow", "清空"))
        self.buttonSave.setText(_translate("MainWindow", "保存"))
        self.labelPosition_2.setText(_translate("MainWindow", "典籍"))

class UI(QMainWindow, MainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.setupUi(self)

    def open(self):
        self.show()

    def close(self):
        self.hide()

if __name__=="__main__":
    app=QApplication(sys.argv)
    UI = UI()
    UI.show()

    sys.exit(app.exec_())
close