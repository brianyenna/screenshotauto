import sys
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ScreenShot(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #Styles
        self.background_style_css = "background-color: rgba(22, 160, 133, 50); border-radius: 1px;"
        self.background_style_css_screenshot = "background-color: rgba(22, 160, 133, 50); border-radius: px;"

        #Window settings
        self.x = 400
        self.y = 30
        self.setFixedSize(600, 200)
        self.move(self.x, self.y)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.SplashScreen | Qt.WindowStaysOnTopHint)

        #Screenshot windows settings
        self.main_screenshot = QLabel(self)
        self.main_screenshot.resize(600, 200)
        self.main_screenshot.setStyleSheet(self.background_style_css)

        #Text label settings
        self.text_label = QLabel(self)
        self.text_label.move(10, 5)
        self.text_label.resize(300, 100)
        self.text_label.setText("This is a test")

        self.show()
    # self.connect(self.le, SIGNAL("tabPressed"),
    #                  self.update)

    def move_window_right(self):
        self.x += 1
        self.show()

    def terminal_ask(self):
        while True:
            print("If you want to close this window, type stop: ")
            get_input = input()
            if get_input.lstrip().rstrip().lower() == "stop":
                self.close_window()
            else:
                print("Invalid Syntax, Try it again.")
            QApplication.processEvents()

    def close_window(self):
        self.close()
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = ScreenShot()
    # MainWindow.show()
    MainWindow.terminal_ask()
    sys.exit(app.exec_())
