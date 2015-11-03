# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(216, 238)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.back = QtGui.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(10, 40, 61, 31))
        self.back.setObjectName(_fromUtf8("back"))
        self.line = QtGui.QLineEdit(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 10, 201, 23))
        self.line.setObjectName(_fromUtf8("line"))
        self.ce = QtGui.QPushButton(self.centralwidget)
        self.ce.setGeometry(QtCore.QRect(80, 40, 61, 31))
        self.ce.setObjectName(_fromUtf8("ce"))
        self.c = QtGui.QPushButton(self.centralwidget)
        self.c.setGeometry(QtCore.QRect(150, 40, 61, 31))
        self.c.setObjectName(_fromUtf8("c"))
        self.seven = QtGui.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(10, 80, 31, 31))
        self.seven.setObjectName(_fromUtf8("seven"))
        self.eight = QtGui.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(50, 80, 31, 31))
        self.eight.setObjectName(_fromUtf8("eight"))
        self.nine = QtGui.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(90, 80, 31, 31))
        self.nine.setObjectName(_fromUtf8("nine"))
        self.div = QtGui.QPushButton(self.centralwidget)
        self.div.setGeometry(QtCore.QRect(130, 80, 31, 31))
        self.div.setObjectName(_fromUtf8("div"))
        self.sqrt = QtGui.QPushButton(self.centralwidget)
        self.sqrt.setGeometry(QtCore.QRect(170, 80, 41, 31))
        self.sqrt.setObjectName(_fromUtf8("sqrt"))
        self.four = QtGui.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(10, 120, 31, 31))
        self.four.setObjectName(_fromUtf8("four"))
        self.mult = QtGui.QPushButton(self.centralwidget)
        self.mult.setGeometry(QtCore.QRect(130, 120, 31, 31))
        self.mult.setObjectName(_fromUtf8("mult"))
        self.squared = QtGui.QPushButton(self.centralwidget)
        self.squared.setGeometry(QtCore.QRect(170, 120, 41, 31))
        self.squared.setObjectName(_fromUtf8("squared"))
        self.five = QtGui.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(50, 120, 31, 31))
        self.five.setObjectName(_fromUtf8("five"))
        self.six = QtGui.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(90, 120, 31, 31))
        self.six.setObjectName(_fromUtf8("six"))
        self.equal = QtGui.QPushButton(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(170, 160, 41, 71))
        self.equal.setObjectName(_fromUtf8("equal"))
        self.two = QtGui.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(50, 160, 31, 31))
        self.two.setObjectName(_fromUtf8("two"))
        self.minus = QtGui.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(130, 160, 31, 31))
        self.minus.setObjectName(_fromUtf8("minus"))
        self.one = QtGui.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(10, 160, 31, 31))
        self.one.setObjectName(_fromUtf8("one"))
        self.three = QtGui.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(90, 160, 31, 31))
        self.three.setObjectName(_fromUtf8("three"))
        self.point = QtGui.QPushButton(self.centralwidget)
        self.point.setGeometry(QtCore.QRect(90, 200, 31, 31))
        self.point.setObjectName(_fromUtf8("point"))
        self.plus = QtGui.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(130, 200, 31, 31))
        self.plus.setObjectName(_fromUtf8("plus"))
        self.zero = QtGui.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(10, 200, 31, 31))
        self.zero.setObjectName(_fromUtf8("zero"))
        self.masmenos = QtGui.QPushButton(self.centralwidget)
        self.masmenos.setGeometry(QtCore.QRect(50, 200, 31, 31))
        self.masmenos.setObjectName(_fromUtf8("masmenos"))
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.back.setText(_translate("MainWindow", "Back", None))
        self.ce.setText(_translate("MainWindow", "CE", None))
        self.c.setText(_translate("MainWindow", "C", None))
        self.seven.setText(_translate("MainWindow", "7", None))
        self.eight.setText(_translate("MainWindow", "8", None))
        self.nine.setText(_translate("MainWindow", "9", None))
        self.div.setText(_translate("MainWindow", "/", None))
        self.sqrt.setText(_translate("MainWindow", "^0.5", None))
        self.four.setText(_translate("MainWindow", "4", None))
        self.mult.setText(_translate("MainWindow", "*", None))
        self.squared.setText(_translate("MainWindow", "^2", None))
        self.five.setText(_translate("MainWindow", "5", None))
        self.six.setText(_translate("MainWindow", "6", None))
        self.equal.setText(_translate("MainWindow", "=", None))
        self.two.setText(_translate("MainWindow", "2", None))
        self.minus.setText(_translate("MainWindow", "-", None))
        self.one.setText(_translate("MainWindow", "1", None))
        self.three.setText(_translate("MainWindow", "3", None))
        self.point.setText(_translate("MainWindow", ".", None))
        self.plus.setText(_translate("MainWindow", "+", None))
        self.zero.setText(_translate("MainWindow", "0", None))
        self.masmenos.setText(_translate("MainWindow", "+/-", None))

