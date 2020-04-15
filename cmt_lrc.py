# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'commend.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time

class MyDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(604, 500)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 611, 301))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "评论"))

    def showcommend(self, content):
        for i in content:
            self.textBrowser.append(i)
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)
            # time.sleep(0.001)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mine = MyDialog()
    dia = QtWidgets.QDialog()
    mine.setupUi(dia)
    c = ('aaaaaaa', 'bbbbbbbbbbbbb', 'asdfsdf','aaa','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a')
    mine.showcommend(c)
    dia.show()
    sys.exit(dia.exec_())
