import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from datetime import datetime

date = datetime.now()
filename = date.strftime('%Y-%m-%d_%H-%M-%S.jpg')
app = QApplication(sys.argv)
QPixmap.grabWindow(QApplication.desktop().winId()).save(filename, 'jpg')
