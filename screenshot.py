import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QLCDNumber, QSlider, QGridLayout
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon, QScreen
from PyQt5.QtCore import Qt, QPoint

class ScreenShot(QMainWindow):
    def __init__(self):
        super().__init__()
        #Window settings
        self.stepMultiplier = 10
        self.stepSize = 1 #number of pixels to move the window by
        geometry = app.desktop().availableGeometry() ##
        self.left = 50
        self.top = 100
        self.minWidth = 10
        self.minHeight = 10
        self.width = 300
        self.height = 300

        # self.height = 200
        self.opacity = 0.5
        self.color = QColor(255,3,3)  #Set RGB colours later
        self.initUI()

    def initUI(self):
        self.refreshWindowGeometry()
        self.setWindowOpacity(self.opacity)
        self.setWindowFlags(Qt.CustomizeWindowHint)
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
        modifier = QApplication.keyboardModifiers()
        key = event.key()
        stepSize = (self.stepSize * self.stepMultiplier) if (modifier == Qt.ShiftModifier) else (self.stepSize)

        #Resize window height and width
        if key == Qt.Key_Left:
            self.resize_window(-stepSize, 0)
        if key == Qt.Key_Right:
            self.resize_window(stepSize, 0)
        if key == Qt.Key_Up:
            self.resize_window(0, -stepSize)
        if key == Qt.Key_Down:
            self.resize_window(0, stepSize)

        #Resize window reference point (self.top and self.left)
        if key == Qt.Key_A:
            self.change_window_reference(-stepSize, 0)
        if key == Qt.Key_D:
            self.change_window_reference(stepSize, 0)
        if key == Qt.Key_W:
            self.change_window_reference(0, -stepSize)
        if key == Qt.Key_S:
            self.change_window_reference(0, stepSize)

        if key == Qt.Key_C:
            self.preview_screen = QApplication.primaryScreen().grabWindow(0,0,300,300)
            self.preview_screen.save('test','jpg')


    def resize_window(self, width, height):
        self.width += width
        self.height += height
        if self.width <= self.minWidth:
            self.width = 10
        if self.height <= self.minHeight:
            self.height = 10
        self.refreshWindowGeometry()

    def change_window_reference(self, inc_x, inc_y):
        self.left += inc_x
        self.top += inc_y
        if self.left <= 0:
            self.left = 0
        if self.top <= 0:
            self.top = 0
        self.refreshWindowGeometry()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = ScreenShot()
    sys.exit(app.exec_())
