import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon
from PyQt5.QtCore import Qt, QPoint

class ScreenShot(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #Window settings
        self.left = 50
        self.top = 100
        self.width = 600
        self.height = 200
        self.opacity = 0.5
        self.color = Qt.green

        self.initUI()

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowOpacity(self.opacity)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SplashScreen | Qt.WindowStaysOnTopHint)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), self.color)
        self.setPalette(p)
        self.setFixedSize(self.width, self.height)

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
