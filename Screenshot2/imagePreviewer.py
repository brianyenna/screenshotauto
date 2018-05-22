from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ImagePreviewer(QLabel):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        
    def keyPressEvent(self, event):
        key = event.key()

        if (key == Qt.Key_Z):
            self.mainWindow.save_screenshot()
        if (key == Qt.Key_C):
            self.mainWindow.clear_screenshot()
        if (key == Qt.Key_Q):
            self.close()
    
    def setPixmap(self, pixmap):
        super().setPixmap(pixmap)
        self.aspectRatio = pixmap.width() / pixmap.height()
        self.originalPm = pixmap

    def resizeEvent(self, event):
        super().setPixmap(self.originalPm.scaled(event.size().width(), event.size().height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))

        

