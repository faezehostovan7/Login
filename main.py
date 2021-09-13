from typing import Counter
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from login import Ui_Form
from panel import Ui_Panel
from loading import Ui_MainLoading


Counter = 0
class MainLoading(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainLoading()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(50)

        self.show()
    def mousePressEvent(self, evt):
        self.olldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()


    def progress(self):
        global Counter
        self.ui.progressBar.setValue(Counter)
        if Counter > 100:
            self.timer.stop()

            self.Panel = RootMain()
            self.Panel.show()
            self.close()


        Counter+=1

    
class Panel(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Panel()
        self.ui.setupUi(self)

    



class RootMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)



        self.ui.pushButtonlogin.clicked.connect(self.LoginPanel)


    def mousePressEvent(self, evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def LoginPanel(self):
        user = self.ui.lineEditusername.text()
        password = self.ui.lineEditpassword.text()

        if user == "admin" and password == "123456":
            self.Paneluser= Panel()
            self.Paneluser.show()

            self.close()

        else:
            print("error user password")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    root = MainLoading()
    sys.exit(app.exec_())
