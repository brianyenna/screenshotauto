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
        self.width = 600
        self.height = 200
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.SplashScreen | Qt.WindowStaysOnTopHint)

    def initUI(self):
        self.setGeometry(self.x, self.y, self.width, self.height)
        #Screenshot windows settings
        self.main_screenshot = QLabel(self)
        self.main_screenshot.resize(self.x, self.y)
        self.main_screenshot.setStyleSheet(self.background_style_css)

        #Text label settings
        self.text_label = QLabel(self)
        self.text_label.move(10, 5)
        self.text_label.resize(300, 100)
        self.text_label.setText("This is a test")

        self.show()

    def keyPressEvent(self, event):
        key = event.key()
        key_map = {Qt.Key_Left: self.move_window(movement = -1, h = True),
                   Qt.Key_Right: self.move_window(movement = 1, h = True),
                   Qt.Key_Down: self.move_window(movement = 1, h = False),
                   Qt.Key_Up: self.move_window(movement = -1, h = False)}
        if key in key_map:
            key_map[key]

    def move_window(movement, h):
        if h: #Horizontal movement
            self.x += movement
            self.initUI()
        else:
            self.y += movement
            self.initUI()

        # key_map = {Qt.Key_Enter:  self.start,  Qt.Key_Return: self.start,
        #            Qt.Key_Escape: self.close,  Qt.Key_P:      self.pause,
        #            Qt.Key_R:      self.reset}
        # key = event.key()
        #
        # # Snake head movement
        # if key in {Qt.Key_Left, Qt.Key_Right,
        #            Qt.Key_Up,   Qt.Key_Down}:
        #     self.key = key
        #
        # # Start, pause, reset or exit game
        # elif key in key_map:
        #     key_map[key]()

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
