# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
from PyQt5 import QtCore, QtGui, QtWidgets

__location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

class Ui_loginScreen(object):
    def setupUi(self, loginScreen):
        loginScreen.setObjectName("loginScreen")
        loginScreen.resize(602, 523)
        loginScreen.setAcceptDrops(False)
        loginScreen.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
"")
        self.centralwidget = QtWidgets.QWidget(loginScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(60, 100, 101, 81))
        self.login_button.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border-color: rgb(0, 0, 128);")
        self.login_button.setText("")
        icon = QtGui.QIcon()
        filelog = os.getcwd()
        print(filelog)
        icon.addPixmap(QtGui.QPixmap(os.path.join(__location__, "account.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(os.path.join(__location__, "account.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.login_button.setIcon(icon)
        self.login_button.setIconSize(QtCore.QSize(150, 100))
        self.login_button.setAutoDefault(False)
        self.login_button.setDefault(True)
        self.login_button.setFlat(False)
        self.login_button.setObjectName("login_button")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(490, 210, 101, 41))
        self.clear_button.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.clear_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(os.path.join(__location__, "Küçük indir (2) .png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(os.path.join(__location__, "Küçük indir (2) .png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.clear_button.setIcon(icon1)
        self.clear_button.setIconSize(QtCore.QSize(100, 85))
        self.clear_button.setObjectName("clear_button")
        self.enter_button = QtWidgets.QPushButton(self.centralwidget)
        self.enter_button.setGeometry(QtCore.QRect(490, 270, 101, 41))
        self.enter_button.setStyleSheet("background-color: rgb(179, 179, 179);")
        self.enter_button.setText("")
        icon2 = QtGui.QIcon()
        icon5 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(os.path.join(__location__, "Küçük images (1) .png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(os.path.join(__location__, "Küçük download .png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(os.path.join(__location__, "Küçük images (1) .png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        
        self.enter_button.setIcon(icon2)
        self.enter_button.setIconSize(QtCore.QSize(100, 100))
        self.enter_button.setObjectName("enter_button")
        self.exit_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button_2.setGeometry(QtCore.QRect(490, 340, 101, 41))
        self.exit_button_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(os.path.join(__location__, "Küçük indir (4) .png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(os.path.join(__location__, "Küçük indir (4) .png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.exit_button_2.setIcon(icon3)
        self.exit_button_2.setIconSize(QtCore.QSize(150, 150))
        self.exit_button_2.setObjectName("exit_button_2")
        self.idnum_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.idnum_edit.setGeometry(QtCore.QRect(220, 240, 241, 41))
        self.idnum_edit.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.idnum_edit.setObjectName("idnum_edit")
        self.password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_edit.setGeometry(QtCore.QRect(220, 330, 241, 41))
        self.password_edit.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.password_edit.setObjectName("password_edit")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.id_label = QtWidgets.QLabel(self.centralwidget)
        self.id_label.setGeometry(QtCore.QRect(30, 240, 151, 41))
        self.id_label.setStyleSheet("background-color: rgb(179, 179, 179);")
        self.id_label.setObjectName("id_label")

        self.id_label2 = QtWidgets.QLabel(self.centralwidget)
        self.id_label2.setGeometry(QtCore.QRect(30, 400, 150, 20))
        self.id_label2.setStyleSheet("background-color: rgb(179, 179, 179);")
        self.id_label2.setObjectName("id_label")

        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(30, 330, 151, 41))
        self.password_label.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.password_label.setObjectName("password_label")
        self.enter_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.enter_button_2.setGeometry(QtCore.QRect(490, 100, 101, 100))
        self.enter_button_2.setStyleSheet("background-color: rgb(179, 179, 179);")
        self.enter_button_2.setText("")
        self.enter_button_2.setIcon(icon5)
        self.enter_button_2.setIconSize(QtCore.QSize(100, 100))
        self.enter_button_2.setObjectName("enter_button_2")
        loginScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loginScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 26))
        self.menubar.setObjectName("menubar")
        loginScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loginScreen)
        self.statusbar.setObjectName("statusbar")
        loginScreen.setStatusBar(self.statusbar)

        self.retranslateUi(loginScreen)
        self.clear_button.clicked.connect(self.idnum_edit.clear) # type: ignore
        self.exit_button_2.clicked.connect(loginScreen.close) # type: ignore
        self.clear_button.clicked.connect(self.password_edit.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(loginScreen)

    def retranslateUi(self, loginScreen):
        _translate = QtCore.QCoreApplication.translate
        loginScreen.setWindowTitle(_translate("loginScreen", "login"))
        self.id_label.setText(_translate("loginScreen", "    ID NUMBER"))
        self.password_label.setText(_translate("loginScreen", "  PASSWORD"))


