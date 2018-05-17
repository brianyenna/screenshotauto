import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QScreen
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel
from datetime import datetime

date = datetime.now()
filename = date.strftime('%Y-%m-%d_%H-%M-%S.jpg')
app = QApplication(sys.argv)
sc=QScreen()
sc.grabWindow(QApplication.desktop().winId()).save(filename, 'jpg')

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        x = 0
        y = 0
        self.text = "x: {0},  y: {1}".format(x, y)
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)
        self.setMouseTracking(True)
        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
