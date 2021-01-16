#!/usr/bin/python

import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QApplication
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pprint
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setStyleSheet('''QToolTip { 
                           background-color: #8ad4ff; 
                           color: black; 
                           border: black solid 10px;
                           }

                        QWidget { 
                           background-color: white; 
                           color: black; 
                           
                           }

                           ''')

        QToolTip.setFont(QFont('Georgia', 11))
        
        pal = QPalette()
        pal.brightText()
        pal.setColor(QPalette.Background, QColor('#348ceb'))
        self.setPalette(pal)

        self.setToolTip('This is QWidget')

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Styled QToolTip')

        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)

        self.x = QWidget()
        self.x.setStyleSheet("background-color:red;")
        self.x.resize(300,100)
        self.x.setToolTip("<img src = \"" + "logo1.png" + "\">")
        pprint.pprint(vars(QToolTip))
        # self.t = QToolTip("fa")

        # self.x.setToolTip(self.t)
        self.vbox.addWidget(self.x)
        
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()