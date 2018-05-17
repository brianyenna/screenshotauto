# import sys
# from PyQt5.QtGui import QPixmap, QApplication
# from PyQt5.QtWidgets import QApplication
# from datetime import datetime
#
# date = datetime.now()
# filename = date.strftime('%Y-%m-%d_%H-%M-%S.jpg')
# app = QApplication(sys.argv)
# QPixmap.grabWindow(QApplication.desktop().winId()).save(filename, 'jpg')


import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.setGeometry(300, 300, 250, 150)
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            print("Killing")
            self.deleteLater()
        elif event.key() == Qt.Key_Enter:
            self.proceed()
        event.accept()

    def proceed(self):
        print("Call Enter Key")

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
