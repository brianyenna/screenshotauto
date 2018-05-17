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

    def refreshWindow(self, left, top, width, height):
        self.setGeometry()

    def keyPressEvent(self, event):
        key = event.key()
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = ScreenShot()
    MainWindow.show()
    sys.exit(app.exec_())
