from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

class ImagePreviewer(QLabel):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow

    def keyPressEvent(self, event):
        key = event.key()

        if (key == Qt.Key_S):
            self.mainWindow.save_screenshot()




