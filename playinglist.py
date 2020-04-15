import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMenu, QAction
from cmt_lrc import MyDialog

class MyLabel(QtWidgets.QLabel):
    def __init__(self,MainWindow,datalist,idx,song_id, parent=None):
        super(MyLabel, self).__init__(parent)
        self.MainWindow = MainWindow
        self.datalist = datalist
        self.idx = idx
        self.song_id = song_id
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenuShow)

    # 双击播放响应
    def mouseDoubleClickEvent(self, e):
        self.MainWindow.menu.datalist = self.datalist
        self.MainWindow.menu.at_playing_list = False
        self.MainWindow.menu.index = self.idx
        self.MainWindow.to_play_song(self.idx)

    # 右键菜单项生成
    def rightMenuShow(self, pos):
        rmenu = QMenu(self)
        self.op1 = rmenu.addAction(QtWidgets.QAction('播放', rmenu))
        self.op3 = rmenu.addAction(QtWidgets.QAction('查看歌词', rmenu))
        self.op4 = rmenu.addAction(QtWidgets.QAction('查看评论', rmenu))
        self.op2 = rmenu.addAction(QtWidgets.QAction('删除', rmenu))

        rmenu.triggered.connect(self.actionHandler)
        rmenu.exec_(QtGui.QCursor.pos())

    # 右键菜单项点击处理
    def actionHandler(self, act):
        # print(act.text())
        if act.text() == '播放':
            self.MainWindow.menu.datalist = self.datalist
            self.MainWindow.menu.at_playing_list = False
            self.MainWindow.menu.index = self.idx
            self.MainWindow.to_play_song(self.idx)
        elif act.text() == '查看评论':
            dia = QtWidgets.QDialog()
            mydia = MyDialog()
            mydia.setupUi(dia)
            comments = self.MainWindow.menu.api.song_comments(self.song_id, limit=100)
            try:
                hotcomments = comments["hotComments"]
                comcomments = comments["comments"]
            except KeyError:
                hotcomments = comcomments = []
            to_display = []
            for one_comment in hotcomments:
                to_display.append('{}:{}\t有{}人觉得很赞\n'.format(one_comment["likedCount"],\
                one_comment["user"]["nickname"], one_comment["content"]))

            mydia.showcommend(to_display)
            dia.show()
            dia.exec()

        elif act.text() == '查看歌词':
            print('emmmmm')
        else:
            pass

    def mouseReleaseEvent(self, e):
        pass

    def focusInEvent(self, e):
        pass

    def focusOutEvent(self, e):
        pass

    def moveEvent(self, e):
        pass

    def leaveEvent(self, e):  # 鼠标离开label
        pass

    def enterEvent(self, e):  # 鼠标移入label
        pass

    def mouseMoveEvent(self, e):
        pass


# 测试用  类，不用管
class TestDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(TestDialog, self).__init__(parent)
        self.statusLabel = MyLabel(self)
        self.statusLabel.setGeometry(QtCore.QRect(95, 220, 151, 41))
        self.statusLabel.setText("hello label")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = TestDialog()
    dialog.show()
    sys.exit(app.exec_())
