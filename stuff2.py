import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt, QPoint, QRect, QSize
from PyQt5.QtGui import QScreen
from PyQt5.QtWidgets import QApplication, QLabel, QRubberBand, QAction

class KpeWindow(QtWidgets.QLabel):
    def __init__(self, parent=None):
        QtWidgets.QLabel.__init__(self,parent)
        main = QtWidgets.QVBoxLayout(self)
        self.selection = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle, self)

        # label = QLabel(self)
        # label.setText('Test the keyPressEvent')
        # main.addWidget(label)

        # self.adjustSize()
        # self.setLayout(main)

    def keyPressEvent(self, event):
        print(event.key())
        if event.key() == QtCore.Qt.Key_Return:
            print('yay')

        #QtWidgets.QMessageBox.warning(self, 'MDI', 'keyPressEvent')
        self.parent().keyPressEvent(event)


    def mousePressEvent(self, event):
        '''
            Mouse is pressed. If selection is visible either set dragging mode (if close to border) or hide selection.
            If selection is not visible make it visible and start at this point.
        '''
        print(event)
        if event.button() == QtCore.Qt.LeftButton:

            position = QtCore.QPoint(event.pos())
            if self.selection.isVisible():
                # visible selection
                if (self.upper_left - position).manhattanLength() < 20:
                    # close to upper left corner, drag it
                    self.mode = "drag_upper_left"
                elif (self.lower_right - position).manhattanLength() < 20:
                    # close to lower right corner, drag it
                    self.mode = "drag_lower_right"
                else:
                    # clicked somewhere else, hide selection
                    self.selection.hide()
            else:
                # no visible selection, start new selection
                self.upper_left = position
                self.lower_right = position
                self.mode = "drag_lower_right"
                self.selection.show()

    def mouseMoveEvent(self, event):
        '''
            Mouse moved. If selection is visible, drag it according to drag mode.
        '''

        if self.selection.isVisible():
            # visible selection
            if self.mode is "drag_lower_right":
                self.lower_right = QtCore.QPoint(event.pos())
            elif self.mode is "drag_upper_left":
                self.upper_left = QtCore.QPoint(event.pos())
            # update geometry
            self.selection.setGeometry(QtCore.QRect(self.upper_left, self.lower_right).normalized())

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        QtWidgets.QMainWindow.__init__(self)
        #self.setWindowTitle('KeyPressEvent Test')
        # main = QtWidgets.QVBoxLayout(self)
        # child = KpeWindow(self)
        # child.setFocusPolicy(Qt.StrongFocus)
        # self.setFocusProxy(child)
        # main.addWidget(child)
        # child.setFocus(True)

        layout = QtWidgets.QVBoxLayout(self)

        label = KpeWindow(self)
        pixmap = QScreen.grabWindow(app.primaryScreen(), app.desktop().winId())
        label.setPixmap(pixmap)
        layout.addWidget(label)
        #new
        label.setFocusPolicy(Qt.StrongFocus)
        self.setFocusProxy(label)
        label.setFocus(True)

        self.setLayout(layout)

        geometry = app.desktop().availableGeometry()

        self.setFixedSize(geometry.width(), geometry.height())


        # self.setWindowFlags( self.windowFlags() | Qt.FramelessWindowHint)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
