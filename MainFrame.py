# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainFrame.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,menu):

        self.index = 0
        self.menu = menu
        self.timer = QtCore.QTimer()


        ########################################################
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(100, 490, 691, 49))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(100, 0, 531, 81))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.radioButton = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton.setGeometry(QtCore.QRect(10, 10, 112, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 30, 112, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 50, 112, 19))
        self.radioButton_3.setObjectName("radioButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(90, 30, 311, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(420, 30, 90, 27))
        self.pushButton.setObjectName("pushButton")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(660, 0, 131, 71))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 30, 90, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(100, 80, 691, 411))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setGeometry(QtCore.QRect(10, 16, 571, 20))
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_4.setGeometry(QtCore.QRect(590, 10, 90, 27))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 571, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 571, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 571, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setGeometry(QtCore.QRect(10, 180, 561, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_5.setGeometry(QtCore.QRect(590, 50, 90, 27))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_6.setGeometry(QtCore.QRect(590, 90, 90, 27))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_7.setGeometry(QtCore.QRect(590, 130, 90, 27))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_8.setGeometry(QtCore.QRect(590, 170, 90, 27))
        self.pushButton_8.setObjectName("pushButton_8")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 101, 541))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 91, 31))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        ##################################################
        self.pushButton.clicked.connect(self.search)

        self.pushButton_3.clicked.connect(self.play_or_pause)

        self.pushButton_4.clicked.connect(self.clicked_0)
        self.pushButton_5.clicked.connect(self.clicked_1)
        self.pushButton_6.clicked.connect(self.clicked_2)
        self.pushButton_7.clicked.connect(self.clicked_3)
        self.pushButton_8.clicked.connect(self.clicked_4)

        self.timer.timeout.connect(self.time_out)
        self.timer.start(1000)

        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "播放/暂停"))
        self.radioButton.setText(_translate("MainWindow", "歌曲名"))
        self.radioButton_2.setText(_translate("MainWindow", "艺术家"))
        self.radioButton_3.setText(_translate("MainWindow", "专辑"))
        self.lineEdit.setToolTip(_translate("MainWindow", "在此键入"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "在此键入数据"))
        self.pushButton.setText(_translate("MainWindow", "搜素"))
        self.pushButton_2.setText(_translate("MainWindow", "登录"))
        self.label.setText(_translate("MainWindow", "此处显示信息"))
        self.pushButton_4.setText(_translate("MainWindow", "确定"))
        self.label_3.setText(_translate("MainWindow", "此处显示信息"))
        self.label_4.setText(_translate("MainWindow", "此处显示信息"))
        self.label_5.setText(_translate("MainWindow", "此处显示信息"))
        self.label_6.setText(_translate("MainWindow", "此处显示信息"))
        self.pushButton_5.setText(_translate("MainWindow", "确定"))
        self.pushButton_6.setText(_translate("MainWindow", "确定"))
        self.pushButton_7.setText(_translate("MainWindow", "确定"))
        self.pushButton_8.setText(_translate("MainWindow", "确定"))
        self.label_2.setText(_translate("MainWindow", "列表"))

    def play_or_pause(self):
        self.menu.at_playing_list = False
        self.to_play_song(self.index)

    def search(self):
        self.menu.at_playing_list = True

        search_info = self.lineEdit.text()
        res = self.menu.get_songs_info(search_info)

        try:
            self.label.setText(res[0])
            self.label_3.setText(res[1])
            self.label_4.setText(res[2])
            self.label_5.setText(res[3])
            self.label_6.setText(res[4])
        except  Exception as e:
            pass
        finally:
            pass


    def clicked_0(self):
        self.index = 0
        self.menu.index = 0
        self.to_play_song(0)

    def clicked_1(self):
        self.index = 1
        self.menu.index = 1
        self.to_play_song(1)


    def clicked_2(self):
        self.index = 2
        self.menu.index = 2
        self.to_play_song(2)

    def clicked_3(self):
        self.index = 3
        self.menu.index = 4
        self.to_play_song(3)

    def clicked_4(self):
        self.index = 4
        self.menu.index = 4
        self.to_play_song(4)

    def to_play_song(self,idx):
        self.menu.play_which_song(idx)

    def time_out(self):
        now,total = self.menu.now_total_time()
        self.progressBar.setValue(now/(total+0.00001)*100)
        self.progressBar.repaint()
        self.progressBar.setFormat('{}/{}'.format(self.shift_time(now),self.shift_time(total)))

        print('{}/{}'.format(self.shift_time(now), self.shift_time(total)))
        
    def shift_time(self,time_val):
        m = int(time_val/60);
        s = int(time_val % 60);
        return '{}:{}'.format(m,s)
