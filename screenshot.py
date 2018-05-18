import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLCDNumber, QSlider, QGridLayout
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon, QScreen
from PyQt5.QtCore import Qt, QPoint

class ScreenShot(QMainWindow):
    def __init__(self):
        super().__init__()
        #Window settings
        self.stepMultiplier = 10
        self.stepBigMultipler = 10
        self.stepSize = 1 #number of pixels to move the window by
        geometry = app.desktop().availableGeometry() ##
        self.left = 50
        self.top = 100
        self.minWidth = 10
        self.minHeight = 10
        self.width = 300
        self.height = 300
        self.opacity = 0.5
        self.color = QColor(255,3,3)  #Set RGB colours later
        self.statusText = "X: {} Y: {} | Width: {} Height: {}"
        self.initUI()

    def initUI(self):
        self.refreshWindowGeometry()
        self.setWindowOpacity(self.opacity)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        
        p = self.palette()
        p.setColor(self.backgroundRole(), self.color)
        self.setAutoFillBackground(True)
        self.setPalette(p)
        
        p = self.statusBar().palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.statusBar().setAutoFillBackground(True)
        self.statusBar().setPalette(p)

        self.show()

    def paintEvent(self, event):
        self.statusBar().clearMessage()
        self.statusBar().showMessage(self.statusText.format(self.left,self.top,self.width,self.height))
        self.statusBar().update()

    def refreshWindowGeometry(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.update()

    def resizeEvent(self, event):
        self.width = event.size().width()
        self.height = event.size().height()
        QMainWindow.resizeEvent(self, event)
        self.update()

    def keyPressEvent(self, event):
        modifier = QApplication.keyboardModifiers()
        key = event.key()
        stepSize = self.stepSize
        stepSize *= self.stepBigMultipler if (modifier & Qt.ShiftModifier) else 1
        stepSize *= self.stepMultiplier if (modifier & Qt.ControlModifier) else 1
        
        #Resize window height and width
        if key == Qt.Key_Left:
            self.resize_window(-stepSize, 0)
        if key == Qt.Key_Right:
            self.resize_window(stepSize, 0)
        if key == Qt.Key_Up:
            self.resize_window(0, -stepSize)
        if key == Qt.Key_Down:
            self.resize_window(0, stepSize)

        #Move window
        if key == Qt.Key_A:
            self.move_window(-stepSize, 0)
        if key == Qt.Key_D:
            self.move_window(stepSize, 0)
        if key == Qt.Key_W:
            self.move_window(0, -stepSize)
        if key == Qt.Key_S:
            self.move_window(0, stepSize)

        if key == Qt.Key_C:
            self.preview_screen = QApplication.primaryScreen().grabWindow(0,0,300,300)
            self.preview_screen.save('test','jpg')

    def mousePressEvent(self, event):
        self.prevPos = event.globalPos()

    def mouseMoveEvent(self, event):        
        modifier = QApplication.keyboardModifiers()
        if modifier == Qt.AltModifier:
            diff = event.globalPos() - self.prevPos
            self.move(self.x() + diff.x(), self.y() + diff.y())
            self.prevPos = event.globalPos()

    def resize_window(self, width, height):
        self.width += width
        self.height += height
        if self.width <= self.minWidth:
            self.width = 10
        if self.height <= self.minHeight:
            self.height = 10
        self.refreshWindowGeometry()

    def move_window(self, inc_x, inc_y):
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
