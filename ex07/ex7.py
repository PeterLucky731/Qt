# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ex7.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 240, 47, 13))
        self.label_3.setObjectName("label_3")
        self.num = QtWidgets.QLineEdit(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(200, 170, 113, 20))
        self.num.setObjectName("num")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 90, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(200, 410, 75, 23))
        self.btn.setObjectName("btn")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 210, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 150, 47, 13))
        self.label.setObjectName("label")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(200, 440, 391, 31))
        self.result.setObjectName("result")
        self.num2 = QtWidgets.QLineEdit(self.centralwidget)
        self.num2.setGeometry(QtCore.QRect(200, 260, 113, 20))
        self.num2.setObjectName("num2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 300, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 330, 47, 13))
        self.label_6.setObjectName("label_6")
        self.num3 = QtWidgets.QLineEdit(self.centralwidget)
        self.num3.setGeometry(QtCore.QRect(200, 350, 113, 20))
        self.num3.setObjectName("num3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label_3.setText(_translate("MainWindow", "Numero 2"))
        self.label_2.setText(_translate("MainWindow", "Média de 3 números"))
        self.btn.setText(_translate("MainWindow", "calcular"))
        self.label_4.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "Numero 1"))
        self.result.setText(_translate("MainWindow", "Resultado"))
        self.label_5.setText(_translate("MainWindow", "+"))
        self.label_6.setText(_translate("MainWindow", "Numero 3"))
