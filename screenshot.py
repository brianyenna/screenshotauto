import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon
from PyQt5.QtCore import Qt, QPoint


class ScreenShot(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #Styles
        self.background_style_css = "background-color: rgba(22, 160, 133, 100); border-radius: 1px;"
        self.background_style_css_screenshot = "background-color: rgba(22, 160, 133, 50); border-radius: 2px;"

        #Window settings
        self.left = 50
        self.top = 100
        self.width = 600
        self.height = 200
        #self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SplashScreen | Qt.WindowStaysOnTopHint)
        self.initUI()

    def initUI(self):
        #Window settings
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        #Screenshot windows settings
        self.main_screenshot = QLabel(self)
        self.main_screenshot.resize(self.left, self.top)
        self.main_screenshot.setStyleSheet(self.background_style_css)

        #Text label settings
        self.text_label = QLabel(self)
        self.text_label.move(10, 5)
        self.text_label.resize(300, 100)
        self.text_label.setText("This is a test")
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            print("Left")
            self.move_window()
        if event.key() == Qt.Key_R:
            print('R')
        # elif event.key() == Qt.Key_Right:
        #     self.proceed_right()
        event.accept()

    # def keyPressEvent(self, event):
    #     key = event.key()
    #     key_map = {Qt.Key_Left: self.move_window(movement = -1, h = True),
    #                Qt.Key_Right: self.move_window(movement = 1, h = True),
    #                Qt.Key_Down: self.move_window(movement = 1, h = False),
    #                Qt.Key_Up: self.move_window(movement = -1, h = False)}
    #     if key in key_map:
    #         key_map[key]
    #     print('Key detected')
    #     event.accept()

    def move_window():
        # if h: #Horizontal movement
        #     self.width += movement
        #     self.initUI()
        # else:
        #     self.height += movement
        #     self.initUI()
        self.width += 1
        self.initUI()
        print('Key Press Event detected')

    def terminal_ask(self):
        while True:
            print("If you want to close this window, type stop: ")
            get_input = input()
            if get_input.lstrip().rstrip().lower() == "stop":
                self.close_window()
            else:
                print("Invalid Syntax, Try it again.")
            QApplication.processEvents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = ScreenShot()
    MainWindow.show()
    MainWindow.terminal_ask()
    sys.exit(app.exec_())
