import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class SimGrid(QtWidgets.QWidget):
    def __init__(self):
        super(SimGrid, self).__init__()
        self.setWindowTitle("My attempt at Grid Layout")

        pixmap1 = QPixmap('data/0.png')
        self.firstPageWidget = QLabel()
        self.firstPageWidget.setPixmap(pixmap1)
        
        pixmap2 = QPixmap('blackline.png')
        self.secondPageWidget = QLabel()
        self.secondPageWidget.setPixmap(pixmap2)
        
        

        self.stackedLayout = QStackedLayout()
        self.stackedLayout.setStackingMode(QStackedLayout.StackAll)
        self.stackedLayout.addWidget(self.firstPageWidget)
        self.stackedLayout.addWidget(self.secondPageWidget)
        
        
        


        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.stackedLayout)
        self.setLayout(self.mainLayout)
        print(self.stackedLayout.currentWidget())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = SimGrid()
    w.show()
    sys.exit(app.exec_())
