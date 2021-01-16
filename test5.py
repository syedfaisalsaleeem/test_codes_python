# number=[1,2,3,4]

# # for index,wa in enumerate(number):
# #     # print(index)
# #     del number[index]

# del number[:]
# print(number)
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        # self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        # self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
        # self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

        # for i in range(1,50):
        #     object = QLabel("TextLabel")
        #     self.vbox.addWidget(object)

        # self.widget.setLayout(self.vbox)

        # #Scroll Area Properties
        # self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.scroll.setWidgetResizable(True)
        # self.scroll.setWidget(self.widget)

        # # self.setCentralWidget(self.scroll)

        # # self.setGeometry(600, 100, 1000, 900)
        # # self.setWindowTitle('Scroll Area Demonstration')
        # self.show()
        
        self.setGeometry(300, 300, 1024, 768)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background:white")
        self.centralwidget.resize(1258, 902)

        self.scroll = QScrollArea(self.centralwidget)
        # self.scroll.setGeometry(0,0,100,100)
        self.frame =QWidget(self.centralwidget)
        self.frame.setStyleSheet("background:pink")
        self.frame.setMinimumSize(1000,668)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.frame)
        # self.frame.setFrameShape(QFrame.StyledPanel)
        # self.frame.setLineWidth(0.6)
        # for i in range(1,500):
        #     object = QLabel("TextLabel",self.frame)
        #     object.setGeometry(20,i,300,300)
            # self.vbox.addWidget(object)

        # self.widget.setLayout(self.vbox)
        self.layout_scrollarea_h1=QHBoxLayout()
        self.layout_scrollarea_h1.setAlignment(Qt.AlignCenter)
        self.widget1=QWidget()
        self.widget1.setFixedSize(300,40)
        # self.widget1.setMinimumWidth(100)
        self.widget1.setStyleSheet("background:yellow")

        self.h1=QHBoxLayout()
        object = QLabel("TextLabel here it is no one",self.widget1)
        self.h1.addStretch(stretch =1)
        self.h1.addWidget(object)
        self.h1.addStretch(stretch =1)
        self.widget1.setLayout(self.h1)

        self.widget2=QWidget()
        self.widget2.setFixedSize(300,40)
        self.widget2.setMinimumWidth(300)
        self.widget2.setStyleSheet("background:yellow")

        self.h2=QHBoxLayout()
        object2 = QLabel("TextLabel here it is no one",self.widget2)
        self.h2.addStretch(stretch =1)
        self.h2.addWidget(object2)
        self.h2.addStretch(stretch =1)
        self.widget2.setLayout(self.h2)

        self.layout_scrollarea_h1.addStretch(stretch =1)
        self.layout_scrollarea_h1.addWidget(self.widget1)
        self.layout_scrollarea_h1.addStretch(stretch =1)
        self.layout_scrollarea_h1.addWidget(self.widget2)
        self.layout_scrollarea_h1.addStretch(stretch =1)

        self.layout_scrollarea_h3=QHBoxLayout()
        self.layout_scrollarea_h3.setAlignment(Qt.AlignTop)
        self.widget3=QWidget()
        self.widget3.setFixedSize(300,40)
        self.widget3.setStyleSheet("background:yellow")

        self.h3=QHBoxLayout()
        object3 = QLabel("TextLabel here it is no onesaddsa ",self.widget3)
        self.h3.addStretch(stretch =1)
        self.h3.addWidget(object3)
        self.h3.addStretch(stretch =1)
        self.widget3.setLayout(self.h3)

        self.widget4=QWidget()
        self.widget4.setFixedSize(300,40)
        self.widget4.setStyleSheet("background:yellow")

        self.h4=QHBoxLayout()
        object4 = QLabel("TextLabel here it is no one",self.widget4)
        self.h4.addStretch(stretch =1)
        self.h4.addWidget(object4)
        self.h4.addStretch(stretch =1)
        self.widget4.setLayout(self.h4)

        self.layout_scrollarea_h3.addStretch(stretch =1)
        self.layout_scrollarea_h3.addWidget(self.widget3)
        self.layout_scrollarea_h3.addStretch(stretch =1)
        self.layout_scrollarea_h3.addWidget(self.widget4)
        self.layout_scrollarea_h3.addStretch(stretch =1)

        
        self.layout_scrollarea_h2=QVBoxLayout(self.frame)
        object2 = QLabel("TextLabel",self.frame)
        object2.setMinimumSize(400,1000)
        object2.setGeometry(20,100,100,30)
        object2.setStyleSheet("background:green")
        object3 = QLabel("TextLabel",self.frame)
        object3.setStyleSheet("background:yellow")
        object3.setGeometry(500,100,130,30)
        self.layout_scrollarea_h2.addWidget(object2)
        self.layout_scrollarea_h2.addWidget(object3)
        self.layout_scrollarea_h2.addLayout(self.layout_scrollarea_h1)
        self.layout_scrollarea_h2.addLayout(self.layout_scrollarea_h3)

        # self.layout_scrollarea_v=QVBoxLayout(self.frame)
        # # self.layout_scrollarea_v.addWidget(QLabel("Test"))
        # # self.layout_scrollarea_v.addLayout(self.layout_scrollarea_h1)
        # # self.layout_scrollarea_v.addLayout(self.layout_scrollarea_h3)
        # self.layout_scrollarea_v.addLayout(self.layout_scrollarea_h2)
        # # self.layout_scrollarea_v.addLayout(self.layout_scrollarea_h2)
        # self.frame.setLayout(self.layout_scrollarea_v)

 
        # self.scroll1 = QScrollArea(self)
        self.frame1 =QWidget(self)
        self.frame1.setStyleSheet("background:red")
        self.frame1.setGeometry(0,0,1024,368)
        # self.scroll1.setWidget(self.frame1) 
        # self.frame1.setFrameShape(QFrame.StyledPanel)
        # self.frame1.setLineWidth(0.6)

        self.button=QPushButton(self.frame1)
        self.button.setText("1234")
        # self.vbox1 = QVBoxLayout()
        # # vbox.addStretch(1)
        # # self.vbox.addWidget(self.button)
        # self.vbox1.addWidget(self.button)
        # self.frame1.setLayout(self.vbox1)
        self.vbox = QVBoxLayout(self)
        self.vbox.addStretch(1)
        # self.vbox.addStretch(1)
        # self.vbox.addStretch(1)
        self.vbox.addWidget(self.button)
        # self.vbox.addWidget(self.frame1)
        self.vbox.addWidget(self.scroll)
        # self.vbox.addLayout(self.vbox1)
        # self.vbox.addStretch(1)
        # self.vbox.addWidget(self.frame1)
        
        self.setLayout(self.vbox)
        # self.setCentralWidget(self.scroll)
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()