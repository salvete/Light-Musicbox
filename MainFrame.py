# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainFrame.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from login import Ui_Dialog
import utils
from playinglist import MyLabel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, menu):
        # 记录播放列表的歌的数量
        self.cnt_song_num = 0
        self.record =[]
        #已经在列表中的歌曲的id
        self.playing_list_id = []
       # self.playing_list_id_sort = []
        cnt_song_num = 0
        self.index = 0
        self.menu = menu
        self.timer = QtCore.QTimer()
        self.username = ''
        self.passwd = ''
        self.check_radio = 1

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
        ##播放列表组件
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 101, 541))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 91, 31))
        self.label_2.setObjectName("label_2")
        # 存放音乐播放列表
        self.frame_6_1 = QtWidgets.QFrame(self.frame_6)
        self.frame_6_1.setGeometry(QtCore.QRect(-1, 39, 101, 501))
        self.frame_6_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6_1.setObjectName("frame_6_1")
        # self.label_100 = QtWidgets.QLabel(self.frame_6_1)

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

        self.pushButton_2.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.pushButton_2.clicked.connect(self.login)

        self.radioButton.setChecked(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Light Musicbox"))
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
        self.menu.at_playing_list = True
        self.to_play_song(self.index)

    def search(self):
        self.menu.at_playing_list = False

        search_info = self.lineEdit.text()

        if self.radioButton.isChecked():
            self.check_radio = 1
            res = self.menu.get_songs_info(search_info, 1)
        elif self.radioButton_2.isChecked():
            self.check_radio = 2
            res = self.menu.get_songs_info(search_info, 2)
        elif self.radioButton_3.isChecked():
            self.check_radio = 3
            res = self.menu.get_songs_info(search_info, 3)
        else:
            self.check_radio = -1
            res = self.menu.get_songs_info('', 3)

        self.label.setText('')
        self.label_3.setText('')
        self.label_4.setText('')
        self.label_5.setText('')
        self.label_6.setText('')


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

    # 点击右侧按钮逻辑处理
    def clicked_0(self):
        self.index = 0
        self.menu.index = 0

        if self.check_radio == 1:
            self.to_play_song(self.index)
            self.add_playing_list(self.menu.datalist, self.index)

        elif self.check_radio == 2:
            self.check_radio = 1
            artist_id = self.menu.datalist[self.index]['artist_id']
            self.menu.datatype = 'songs'
            songs = self.menu.api.artists(artist_id)
            self.menu.datalist = self.menu.api.dig_info(songs,'songs')
            res = []
            for idxx, val in enumerate(self.menu.datalist):
                res.append('{}(歌曲名)-{}(艺术家))'.format(val['song_name'], val['artist']))
                if idxx > 10:
                    break;
            self.label.setText('')
            self.label_3.setText('')
            self.label_4.setText('')
            self.label_5.setText('')
            self.label_6.setText('')

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

        elif self.check_radio == 3:
            self.check_radio = 1
            album_id = self.menu.datalist[self.index]["album_id"]
            songs = self.menu.api.album(album_id)
            self.menu.datatype = "songs"
            self.menu.datalist = self.menu.api.dig_info(songs, "songs")
            res = []
            for idxx, val in enumerate(self.menu.datalist):
                res.append('{}(歌曲名)-{}(艺术家))'.format(val['song_name'], val['artist']))
                if idxx > 10:
                    break;
            self.label.setText('')
            self.label_3.setText('')
            self.label_4.setText('')
            self.label_5.setText('')
            self.label_6.setText('')

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

        else:
            pass

    def clicked_1(self):
        self.index = 1
        self.menu.index = 1

        if self.check_radio == 1:
            self.to_play_song(self.index)
            self.add_playing_list(self.menu.datalist,self.index)

        elif self.check_radio == 2:
            self.check_radio = 1
            artist_id = self.menu.datalist[self.index]['artist_id']
            self.menu.datatype = 'songs'
            songs = self.menu.api.artists(artist_id)
            self.menu.datalist = self.menu.api.dig_info(songs, 'songs')
            res = []
            for idxx, val in enumerate(self.menu.datalist):
                res.append('{}(歌曲名)-{}(艺术家))'.format(val['song_name'], val['artist']))
                if idxx > 10:
                    break;
            self.label.setText('')
            self.label_3.setText('')
            self.label_4.setText('')
            self.label_5.setText('')
            self.label_6.setText('')

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

        elif self.check_radio == 3:
            self.check_radio = 1
            album_id = self.menu.datalist[self.index]["album_id"]
            songs = self.menu.api.album(album_id)
            self.menu.datatype = "songs"
            self.menu.datalist = self.menu.api.dig_info(songs, "songs")
            res = []
            for idxx, val in enumerate(self.menu.datalist):
                res.append('{}(歌曲名)-{}(艺术家))'.format(val['song_name'], val['artist']))
                if idxx > 10:
                    break;
            self.label.setText('')
            self.label_3.setText('')
            self.label_4.setText('')
            self.label_5.setText('')
            self.label_6.setText('')

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

        else:
            pass

    def clicked_2(self):
        self.index = 2
        self.menu.index = 2

        if self.check_radio == 1:
            self.to_play_song(self.index)
            self.add_playing_list(self.menu.datalist, self.index)


        elif self.check_radio == 2:
            self.check_radio = 1
            artist_id = self.menu.datalist[self.index]['artist_id']
            self.menu.datatype = 'songs'
            songs = self.menu.api.artists(artist_id)
            self.menu.datalist = self.menu.api.dig_info(songs, 'songs')
            res = []
            for idxx, val in enumerate(self.menu.datalist):
                res.append('{}(歌曲名)-{}(艺术家))'.format(val['song_name'], val['artist']))
                if idxx > 10:
                    break;
            self.label.setText('')
            self.label_3.setText('')
            self.label_4.setText('')
            self.label_5.setText('')
            self.label_6.setText('')

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

        elif self.check_radio == 3:
            self.check_radio = 1
            album_id = self.menu.datalist[self.index]["album_id"]
            songs = self.menu.api.album(album_id)
            self.menu.datatype = "songs"
            self.menu.datalist = self.menu.api.dig_info(songs, "songs")
            res = []
            for idxx, val in enumerate(self.menu.datalist):
                res.append('{}(歌曲名)-{}(艺术家))'.format(val['song_name'], val['artist']))
                if idxx > 10:
                    break;
            self.label.setText('')
            self.label_3.setText('')
            self.label_4.setText('')
            self.label_5.setText('')
            self.label_6.setText('')

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

        else:
            pass

    def clicked_3(self):
        self.index = 3
        self.menu.index = 4

        if self.check_radio == 1:
            self.to_play_song(self.index)
            self.add_playing_list(self.menu.datalist, self.index)

        elif self.check_radio == 2:
            self.check_radio = 1
            artist_id = self.menu.datalist[self.index]['artist_id']
            self.menu.datatype = 'songs'
            songs = self.menu.api.artists(artist_id)
            self.menu.datalist = self.menu.api.dig_info(songs, 'songs')
            res = []
            for idxx, val in enumerate(self.menu.datalist):
                res.append('{}(歌曲名)-{}(艺术家))'.format(val['song_name'], val['artist']))
                if idxx > 10:
                    break;
            self.label.setText('')
            self.label_3.setText('')
            self.label_4.setText('')
            self.label_5.setText('')
            self.label_6.setText('')

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

        elif self.check_radio == 3:
            self.check_radio = 1
            album_id = self.menu.datalist[self.index]["album_id"]
            songs = self.menu.api.album(album_id)
            self.menu.datatype = "songs"
            self.menu.datalist = self.menu.api.dig_info(songs, "songs")
            res = []
            for idxx, val in enumerate(self.menu.datalist):
                res.append('{}(歌曲名)-{}(艺术家))'.format(val['song_name'], val['artist']))
                if idxx > 10:
                    break;
            self.label.setText('')
            self.label_3.setText('')
            self.label_4.setText('')
            self.label_5.setText('')
            self.label_6.setText('')

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

        else:
            pass

    def clicked_4(self):
        self.index = 4
        self.menu.index = 4

        if self.check_radio == 1:
            self.to_play_song(self.index)
            self.add_playing_list(self.menu.datalist, self.index)

        elif self.check_radio == 2:
            self.check_radio = 1
            artist_id = self.menu.datalist[self.index]['artist_id']
            self.menu.datatype = 'songs'
            songs = self.menu.api.artists(artist_id)
            self.menu.datalist = self.menu.api.dig_info(songs, 'songs')
            res = []
            for idxx, val in enumerate(self.menu.datalist):
                res.append('{}(歌曲名)-{}(艺术家))'.format(val['song_name'], val['artist']))
                if idxx > 10:
                    break;
            self.label.setText('')
            self.label_3.setText('')
            self.label_4.setText('')
            self.label_5.setText('')
            self.label_6.setText('')

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

        elif self.check_radio == 3:
            self.check_radio = 1
            album_id = self.menu.datalist[self.index]["album_id"]
            songs = self.menu.api.album(album_id)
            self.menu.datatype = "songs"
            self.menu.datalist = self.menu.api.dig_info(songs, "songs")
            res = []
            for idxx, val in enumerate(self.menu.datalist):
                res.append('{}(歌曲名)-{}(艺术家))'.format(val['song_name'], val['artist']))
                if idxx > 10:
                    break;
            self.label.setText('')
            self.label_3.setText('')
            self.label_4.setText('')
            self.label_5.setText('')
            self.label_6.setText('')

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

        else:
            pass

    def to_play_song(self, idx):
        self.menu.play_which_song(idx)

    def time_out(self):
        now, total = self.menu.now_total_time()

        self.progressBar.setValue(now / (total + 0.00001) * 100)
        self.progressBar.repaint()
        self.progressBar.setFormat('{}/{}'.format(self.shift_time(now), self.shift_time(total)))

        # print('{}/{}'.format(self.shift_time(now), self.shift_time(total)))

    def shift_time(self, time_val):
        m = int(time_val / 60);
        s = int(time_val % 60);
        return '{}:{}'.format(m, s)

    ##将当前播放到歌曲添加到播放列表
    def add_playing_list(self,datalist,idx):
        song_id = self.menu.storage.database['player_info']['player_list'][idx]
        song_name = self.menu.storage.database['songs'].get(song_id, {})['song_name']
        
        if song_id not in self.playing_list_id:
            self.playing_list_id.append(song_id)           
            self.cnt_song_num = self.cnt_song_num + 1
            # self.wd = QtWidgets.QLabel(self.frame_6_1)
            self.wd = MyLabel(MainWindow=self,datalist=datalist,idx=idx,song_id=song_id,now_playing_list_id=self.playing_list_id,parent=self.frame_6_1)
            self.wd.setGeometry(QtCore.QRect(0, 0 + 31 * (self.cnt_song_num - 1), 101, 31))
            self.wd.setObjectName("pushbutton_100")
            self.wd.setText(song_name)
            self.wd.show()
            self.record.append(self.wd)
           # print(self.record)
        else:
            pass
    def paint_list(self):
        for aa in self.record:
            aa.deny()
        self.cnt_song_num = 0
        self.record.clear()
        for ev in self.playing_list_id:
            datalist=self.menu.datalist
            idx=self.index
            song_id = ev
            song_name = self.menu.storage.database['songs'].get(song_id, {})['song_name']
            self.cnt_song_num += 1
            self.wd = MyLabel(MainWindow=self,datalist=datalist,idx=idx,song_id=song_id,now_playing_list_id=self.playing_list_id,parent=self.frame_6_1)
            self.wd.setGeometry(QtCore.QRect(0, 0 + 31 * (self.cnt_song_num - 1), 101, 31))
            self.wd.setObjectName("pushbutton_100")
            self.wd.setText(song_name)
            self.wd.show()
            self.record.append(self.wd)
       # print('left:')
       # print(self.cnt_song_num)

    def closeEvent(self, e):
        self.menu.player.stop()
        self.menu.storage.save()
        self.menu.api.logout()

    def login(self):

        dia = QtWidgets.QDialog()
        lgin = Ui_Dialog()
        lgin.setupUi(dia, self)
        dia.show()
        dia.exec()

        if self.menu.to_login(self.username, self.passwd):
            utils.notify('登录成功')
            self.pushButton_2.setStyleSheet\
                ("background-color:#99FFFF;border:2px groove gray;border-radius:10px;padding:2px 4px;")
            self.pushButton_2.setText(self.menu.user['nickname'])

        else:
            utils.notify('登录失败，请重新登录')







