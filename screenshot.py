import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon
from PyQt5.QtCore import Qt, QPoint

class ScreenShot(QWidget):
    def __init__(self):
        super().__init__()
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
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.SplashScreen | Qt.WindowStaysOnTopHint)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), self.color)
        self.setPalette(p)
        self.show()

    def keyPressEvent(self, event):
        key = event.key()
        print(key)
        if key == Qt.Key_Left:
            print("Left")
            self.move_window()
        if key == Qt.Key_Right:
            print('Right')
            self.move_window()
        event.accept()

    def move_window(self):
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

    def close_window(self):
        self.close()
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = ScreenShot()
    MainWindow.terminal_ask()
    sys.exit(app.exec_())
