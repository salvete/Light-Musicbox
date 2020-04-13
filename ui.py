import  sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from MainFrame import Ui_MainWindow
from menu import  Menu
class UI(QMainWindow,Ui_MainWindow):
    def __init__(self,menu,parent=None):
        super(UI,self).__init__(parent)
        self.setupUi(self,menu)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = Menu()
    ui = UI(menu)
    ui.show()
    sys.exit(app.exec_())