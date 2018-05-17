import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon
from PyQt5.QtCore import Qt, QPoint

class ScreenShot(QMainWindow):
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
        self.refreshWindowGeometry()
        self.setWindowOpacity(self.opacity)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), self.color)
        self.setPalette(p)
        self.show()

    def refreshWindowGeometry(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def resizeEvent(self, event):
        self.width = event.size().width()
        self.height = event.size().height()
        QMainWindow.resizeEvent(self, event)

    def keyPressEvent(self, event):
        key = event.key()
        print(key)
        if key == Qt.Key_Left:
            self.resize_window(-10, 0)
        if key == Qt.Key_Right:
            self.resize_window(10, 0)
        if key == Qt.Key_Up:
            self.resize_window(0, -10)
        if key == Qt.Key_Down:
            self.resize_window(0, 10)
    
    def resize_window(self, width, height):
        self.width += width
        self.height += height
        if self.width <= 0:
            self.width = 10
        if self.height <= 0:
            self.height = 10
        self.refreshWindowGeometry()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = ScreenShot()
    sys.exit(app.exec_())
