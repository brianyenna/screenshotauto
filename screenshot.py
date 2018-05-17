import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QLCDNumber, QSlider, QGridLayout
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon
from PyQt5.QtCore import Qt, QPoint

class ScreenShot(QWidget):
    def __init__(self):
        super().__init__()
        #Window settings
        self.big_steps = False
        self.left = 50
        self.top = 100
        self.width = 600
        self.height = 200
        self.opacity = 0.5
        self.color = QColor(255,3,3)  #Set RGB colours later
        self.initUI()

    def initUI(self):
        self.create_mouse_position_label()
        self.refreshWindowGeometry()
        self.setWindowOpacity(self.opacity)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), self.color)
        self.setPalette(p)
        self.show()

    def create_mouse_position_label(self):
        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_text = 'X: {}, Y: {}'.format(self.mouse_x, self.mouse_y)
        self.mouse_background_style_css = "background-color: rgba(22, 160, 133, 50); border-radius: px;"

        self.mouse_tracker = QLabel(self)
        self.mouse_tracker.resize(200,200)
        self.mouse_tracker.setStyleSheet(self.mouse_background_style_css)
        self.mouse_tracker.setText(self.mouse_text)
        self.mouse_tracker.move(10,10)

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
