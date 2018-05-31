import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog, QStatusBar, QWidget, QDesktopWidget
from PyQt5.QtGui import QColor, QPixmap, QScreen, QPainter, QBrush
from PyQt5.QtCore import Qt, QPoint, QDir, QRect
from imagePreviewer import ImagePreviewer

class ScreenShot(QMainWindow):
    def __init__(self):
        super().__init__()
        #Window settings
        self.availableGeometry = app.desktop().availableGeometry()
        self.screenGeometry = QDesktopWidget().screenGeometry(-1)
        self.left = 0
        self.top = 0
        self.minWidth = 0
        self.minHeight = 0
        self.maxWidth = self.availableGeometry.width()
        self.maxHeight = self.availableGeometry.height()
        self.width = self.maxWidth
        self.height = self.maxHeight
        self.opacity = 0.3
        self.color = QColor(255,255,255)  #Set RGB colours later
        self.taking_screenshot = False #Boolean. Set to True when screenshot process is occuring
        self.statusText = "X1: {} Y1: {} | X2: {} Y2: {} | Width: {} Height: {}"
        
        #Step Multipliers
        self.stepMultiplier = 10
        self.stepBigMultipler = 10
        self.stepSize = 1 #number of pixels to move the window by

        #Mouse cursor
        self.begin = QPoint(0,0)
        self.end = QPoint(0,0)
        self.x_compensate = self.availableGeometry.x() - self.screenGeometry.x()
        self.y_compensate = self.availableGeometry.y() - self.screenGeometry.y()
        self.begin_x_definitive = None
        self.begin_y_definitive = None
        self.end_x_definitive = None
        self.end_y_definitive = None
        self.screenshot_width = None
        self.screenshot_height = None

        self.initUI()

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowOpacity(self.opacity)
        self.setAutoFillBackground(True)
        
        #Window Color
        p = self.palette()
        p.setColor(self.backgroundRole(), self.color)
        self.setPalette(p)
        
        #Status Bar Color
        p = self.statusBar().palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.statusBar().setAutoFillBackground(True)
        self.statusBar().setPalette(p)

        #Image Previewer
        self.imagePreviewer = ImagePreviewer(self)
        self.imagePreviewer.setWindowTitle("Screenshot preview")
        self.imagePreviewer.hide()

        self.show()

    def paintEvent(self, event):
        qp = QPainter(self)
        if self.taking_screenshot:
            br = QBrush(QColor(125, 120, 100, 100))
        else:
            br = QBrush(QColor(255, 15, 123, 40))
        qp.setBrush(br)
        qp.begin(self)
        qp.drawRect(QRect(self.begin, self.end))
        qp.end()

        self.statusBar().clearMessage()
        self.statusBar().showMessage(self.statusText.format(self.begin_x_definitive,self.begin_y_definitive,self.end_x_definitive, self.end_y_definitive,self.screenshot_width,self.screenshot_height))
        self.statusBar().update()

    def resizeEvent(self, event):
        self.width = event.size().width()
        self.height = event.size().height()
        self.update()
    
    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.end = event.pos()

        #Top Left
        self.begin_x_definitive = min(self.begin.x(), self.end.x())
        self.begin_y_definitive = min(self.begin.y(), self.end.y())
        #Bottom Right
        self.end_x_definitive = max(self.begin.x(), self.end.x())
        self.end_y_definitive = max(self.begin.y(), self.end.y())

        #This ensures that no matter in which direction the user drags the screenshot box, self.begin always refers to the top left hand corner while self.end always refers to the bottom right hand corner
        self.begin = QPoint(self.begin_x_definitive, self.begin_y_definitive)
        self.end = QPoint(self.end_x_definitive, self.end_y_definitive)

        #Update screenshot width and height
        self.screenshot_width = self.end.x() - self.begin.x()
        self.screenshot_height = self.end.y() - self.begin.y()

        self.update()

    def keyPressEvent(self, event):
        modifier = QApplication.keyboardModifiers()
        key = event.key()
        stepSize = self.stepSize
        stepSize *= self.stepBigMultipler if (modifier & Qt.ShiftModifier) else 1
        stepSize *= self.stepMultiplier if (modifier & Qt.ControlModifier) else 1
        
        #Resize end point height and width (mouseReleaseEvent)
        if key == Qt.Key_Left:
            self.resize_end_point(-stepSize, 0)
        if key == Qt.Key_Right:
            self.resize_end_point(stepSize, 0)
        if key == Qt.Key_Up:
            self.resize_end_point(0, -stepSize)
        if key == Qt.Key_Down:
            self.resize_end_point(0, stepSize)
        
        ##Resize begin point height and width (mousePressEvent)
        if key == Qt.Key_A:
            self.resize_start_point(-stepSize, 0)
        if key == Qt.Key_D:
            self.resize_start_point(stepSize, 0)
        if key == Qt.Key_W:
            self.resize_start_point(0, -stepSize)
        if key == Qt.Key_S:
            self.resize_start_point(0, stepSize)
        
        #Screenshot Functions/Miscellaneous
        if key == Qt.Key_Space:
            self.take_screenshot()
        if key == Qt.Key_Z:
            self.save_screenshot()
        if key == Qt.Key_C:
            self.change_transparent()
            self.clear_screenshot()
        if key == Qt.Key_Q:
            self.close()
    
    def resize_start_point(self, inc_x, inc_y): #Top left
        new_x = self.begin.x() + inc_x
        new_y = self.begin.y() + inc_y
        if new_x < 0:
            new_x = 0
        if new_y < 0:
            new_y = 0
        self.begin.setX(new_x)
        self.begin.setY(new_y)
        self.screenshot_width = self.end.x() - self.begin.x()
        self.screenshot_height = self.end.y() - self.begin.y()
        self.update()

    def resize_end_point(self, inc_x, inc_y): #Bottom right
        new_x = self.end.x() + inc_x
        new_y = self.end.y() + inc_y
        if new_x > self.maxWidth:
            new_x = self.maxWidth
        if new_y > self.maxHeight:
            new_y = self.maxHeight
        self.end.setX(new_x)
        self.end.setY(new_y)
        self.screenshot_width = self.end.x() - self.begin.x()
        self.screenshot_height = self.end.y() - self.begin.y()
        self.update()

    def clear_screenshot(self):
        self.imagePreviewer.hide()
        self.pixmap = None

    def take_screenshot(self):
        screen = app.primaryScreen()
        self.hide()
        #If not screenshot window is set, the program defaults to taking a screenshot of the entire window
        if any(i == None for i in [self.begin.x(), self.begin.y(), self.screenshot_height, self.screenshot_width]):
            self.pixmap = screen.grabWindow(MainWindow.id, 0, 0, self.maxWidth, self.maxHeight)
        else:
            self.pixmap = screen.grabWindow(MainWindow.id, self.begin.x(), self.begin.y()+2*self.y_compensate, self.screenshot_width, self.screenshot_height)
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
            take_screenshot()
            save_screenshot()
        self.done = False

    def change_transparent(self):
        self.taking_screenshot = not self.taking_screenshot
        if self.taking_screenshot:
            self.opacity = 0
            self.initUI()
            self.update()
        else:
            self.opacity = 0.3
            self.initUI()
            self.update()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = ScreenShot()
    MainWindow.id = QApplication.desktop().winId()
    sys.exit(app.exec_())
