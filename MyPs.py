# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyPs.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MyPs")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OpenFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.OpenFileButton.setGeometry(QtCore.QRect(680, 10, 113, 32))
        self.OpenFileButton.setObjectName("OpenFileButton")
        self.SaveFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveFileButton.setGeometry(QtCore.QRect(680, 60, 113, 32))
        self.SaveFileButton.setObjectName("SaveFileButton")
        self.GrayImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.GrayImageButton.setGeometry(QtCore.QRect(680, 110, 113, 32))
        self.GrayImageButton.setObjectName("GrayImageButton")
        self.BinaryImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.BinaryImageButton.setGeometry(QtCore.QRect(680, 160, 113, 32))
        self.BinaryImageButton.setObjectName("BinaryImageButton")
        self.LeftRotateImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.LeftRotateImageButton.setGeometry(QtCore.QRect(680, 210, 113, 32))
        self.LeftRotateImageButton.setObjectName("LeftRotateImageButton")
        self.Pic = QtWidgets.QLabel(self.centralwidget)
        self.Pic.setGeometry(QtCore.QRect(20, 40, 660, 520))
        self.Pic.setText("")
        self.Pic.setObjectName("Pic")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MyPs", "MyPs"))
        self.OpenFileButton.setText(_translate("MyPs", "打开图像"))
        self.SaveFileButton.setText(_translate("MyPs", "保存图像"))
        self.GrayImageButton.setText(_translate("MyPs", "灰度图像"))
        self.BinaryImageButton.setText(_translate("MyPs", "二值图像"))
        self.LeftRotateImageButton.setText(_translate("MyPs", "向左旋转"))

