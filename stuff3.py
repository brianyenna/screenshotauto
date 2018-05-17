import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QBrush, QColor

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30,30,600,400)
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.stop = False
        self.show()


    def paintEvent(self, event):
        qp = QPainter(self)
        br = QBrush(QColor(100, 10, 10, 40))
        qp.setBrush(br)
        # if self.stop:
        #     qp.begin(self)
        #     qp.drawRect(self.begin)
        qp.begin(self)
        qp.drawRect(QtCore.QRect(self.begin, self.end))
        # qp.drawRect(100,100,100,100)
        qp.end()

    def mousePressEvent(self, event):
        self.begin = event.pos()
        # self.end = event.pos()
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        # self.begin = event.pos()
        self.end = event.pos()
        self.stop = True
        self.update()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())
