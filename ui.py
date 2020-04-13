import  sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from MainFrame import Ui_MainWindow

class UI(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(UI,self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec_())