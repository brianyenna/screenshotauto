import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog, QStatusBar, QWidget
from PyQt5.QtGui import QColor, QPixmap, QScreen
from PyQt5.QtCore import Qt, QPoint, QDir
from imagePreviewer import ImagePreviewer

class ScreenShot(QMainWindow):
    def __init__(self):
        super().__init__()
        #Window settings
        self.stepMultiplier = 10
        self.stepBigMultipler = 10
        self.stepSize = 1 #number of pixels to move the window by
        self.left = 50
        self.top = 100
        self.minWidth = 10
        self.minHeight = 10
        self.oldGeometry = [self.top,self.left,self.width,self.height]
        self.maxWidth = self.availableGeometry.width()
        self.maxHeight = self.availableGeometry.height()
        self.width = self.maxWidth
        self.height = self.maxHeight
        self.opacity = 0.5
        self.color = QColor(10,10,10)  #Set RGB colours later
        self.taking_screenshot = False #Boolean. Set to True when screenshot process is occuring
        self.statusText = "X: {} Y: {} | Width: {} Height: {}"
        self.initUI()

    def initUI(self):
        self.refreshWindowGeometry()
        self.setWindowOpacity(self.opacity)
        # self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)

        p = self.palette()
        p.setColor(self.backgroundRole(), self.color)
        self.setAutoFillBackground(True)
        self.setPalette(p)
        
        p = self.statusBar().palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.statusBar().setAutoFillBackground(True)
        self.statusBar().setPalette(p)

        self.imagePreviewer = ImagePreviewer(self)
        self.imagePreviewer.setWindowTitle("Screenshot preview")
        self.imagePreviewer.hide()
        self.show()

        self.maximized = False

    def refreshWindowGeometry(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.update()

    def paintEvent(self, event):
        self.statusBar().clearMessage()
        self.statusBar().showMessage(self.statusText.format(self.left,self.top,self.width,self.height))
        self.statusBar().update()

    def resizeEvent(self, event):
        self.width = event.size().width()
        self.height = event.size().height()
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
        
        if key == Qt.Key_Space:
            self.take_screenshot()
        if key == Qt.Key_Z:
            self.save_screenshot()
        if key == Qt.Key_C:
            self.clear_screenshot()
        if key == Qt.Key_Q:
            self.close()
        if key == Qt.Key_F:
            self.maximize_window()

    def mousePressEvent(self, event):
        self.prevPos = event.globalPos()

    def mouseMoveEvent(self, event):        
        diff = event.globalPos() - self.prevPos
        self.move_window(diff.x(), diff.y())
        self.prevPos = event.globalPos()

    def maximize_window(self):
        if self.maximized:
            self.top = self.oldGeometry[0]
            self.left = self.oldGeometry[1]
            self.width = self.oldGeometry[2]
            self.height = self.oldGeometry[3]
            self.showNormal()
            self.maximized = False
        else:
            self.oldGeometry = [self.top, self.left, self.width, self.height]
            self.top = 0
            self.left = 0
            self.showMaximized()
            self.maximized = True
        
        self.refreshWindowGeometry()

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

    def clear_screenshot(self):
        self.imagePreviewer.hide()
        self.pixmap = None

    def take_screenshot(self):
        screen = QApplication.primaryScreen()
        self.hide()
        self.pixmap = screen.grabWindow(self.id, self.left, self.top, self.width, self.height)
        self.show()
        self.imagePreviewer.setPixmap(self.pixmap)
        self.imagePreviewer.adjustSize()
        self.imagePreviewer.resize(self.imagePreviewer.sizeHint())
        self.imagePreviewer.show()
        self.activateWindow()
        self.done = True
    
    def save_screenshot(self):
        if self.done:
            filename = QFileDialog.getSaveFileName(self, "Save As", QDir.currentPath(), "PNG Files (*.png)")
            if filename:
                self.pixmap.save(filename[0], "png")

            self.imagePreviewer.hide()
        else:
            self.take_screenshot()
            self.save_screenshot()
        self.done = False



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = ScreenShot()
    MainWindow.id = QApplication.desktop().winId()
    sys.exit(app.exec_())
