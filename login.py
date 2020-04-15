# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import  sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog,Mainwindow):
        Dialog.setObjectName("登录")
        Dialog.resize(400, 300)
        self.dialog = Dialog
        self.MainWindow = Mainwindow
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 10, 151, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 72, 15))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 50, 191, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 110, 191, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 190, 90, 27))
        self.pushButton.setObjectName("pushButton")

        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.clicked_fun)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "登录"))
        self.label.setText(_translate("Dialog", "请输入相关登录信息"))
        self.label_2.setText(_translate("Dialog", "账号："))
        self.label_3.setText(_translate("Dialog", "密码："))
        self.pushButton.setText(_translate("Dialog", "确定"))

    def clicked_fun(self):
        username = self.lineEdit.text()
        passwd = self.lineEdit_2.text()
        self.MainWindow.username = username
        self.MainWindow.passwd = passwd
        # print(self.MainWindow.username,self.MainWindow.passwd,sep=' ')
        self.dialog.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mine = Ui_Dialog()
    dia = QtWidgets.QDialog()
    mine.setupUi(dia)
    dia.show()
    sys.exit(dia.exec_())


