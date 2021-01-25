# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import pyqtSlot
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# class App(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.title = 'PyQt5 layout - pythonspot.com'
#         self.left = 10
#         self.top = 10
#         self.width = 1024
#         self.height = 768
#         self.initUI()
        
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setMinimumSize(1024, 768)
#         self.showMaximized()
#         # self.setGeometry(self.left, self.top, self.width, self.height)
        
#         self.createGridLayout()
        
#         windowLayout = QVBoxLayout()
#         windowLayout.setContentsMargins(0,0,0,0)
#         # windowLayout.setSpacing(0)
#         windowLayout.addWidget(self.horizontalGroupBox)
#         self.setLayout(windowLayout)
        
#         self.show()
    
#     def createGridLayout(self):
#         self.horizontalGroupBox = QFrame()
#         self.horizontalGroupBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         self.widget1 = QWidget()
#         self.widget1.setStyleSheet("background:blue")

#         self.widget2 = QWidget()
#         self.widget2.setStyleSheet("background:#F8F8F8")

#         widget2_1 = QWidget()
#         widget2_1.setStyleSheet("background:pink")

#         widget2_2 = QWidget()
#         widget2_2.setStyleSheet("background:green")

#         widget2_3 = QWidget()
#         widget2_3.setStyleSheet("background:gray")

#         widget2_4 = QWidget()
#         widget2_4.setStyleSheet("background:black")

#         self.widget3 = QWidget()
#         self.widget3.setStyleSheet("background:yellow")
        
#         layout = QGridLayout()
#         layout.setContentsMargins(0,0,0,0)
#         layout.setSpacing(0)
#         layout.setColumnStretch(0, 1)
#         layout.setColumnStretch(1, 4)
#         layout.setColumnStretch(2, 1)
        
#         layout.setRowStretch(0, 1)
#         layout.setRowStretch(1, 5)
#         layout.setRowStretch(2, 2)
#         layout.setRowStretch(3, 5)
#         # layout.setRowStretch(1, 2)
#         # layout.setRowStretch(2, 1)
        
#         layout.addWidget(self.widget1,0,0,0,1) #1st row 1st column expand to 2nd row 2nd column  ##if we place 0 in expand it will expand full
#         layout.addWidget(self.widget2,0,1)
#         layout.addWidget(widget2_1,1,1)
#         layout.addWidget(widget2_2,2,1)
#         layout.addWidget(widget2_3,3,1)
#         layout.addWidget(self.widget3,0,2,0,1)

#         self.load_data_layout()
#         self.main_top()
#         self.discover_layout()
#         self.horizontalGroupBox.setLayout(layout)

#     def discover_layout(self):
#         self.discover_grid_layout = QGridLayout()
#         self.discover_grid_layout.setContentsMargins(0,0,0,0)
#         self.discover_grid_layout.setSpacing(0)
#         self.widget3.setLayout(self.discover_grid_layout)

#         self.discover_widget1 = QFrame()
#         self.discover_widget1.setStyleSheet("background:#EBEBEB")
#         self.discover_widget2 = QFrame()
#         self.discover_widget2.setStyleSheet("background:#EBEBEB")

#         self.discover_grid_layout.setColumnStretch(0, 1)
        
#         self.discover_grid_layout.setRowStretch(0, 1)
#         self.discover_grid_layout.setRowStretch(1, 10)
        
#         self.discover_grid_layout.addWidget(self.discover_widget1)
#         self.discover_grid_layout.addWidget(self.discover_widget2)

#         self.discover()

#     def discover(self):
#         self.vbox = QVBoxLayout()
#         self.discover_label = QLabel("Discover")
#         self.discover_label.setStyleSheet('color:#6A6A6A;margin-bottom:8px')
#         self.discover_label.setFont(QFont('Arial', 20))
# #u'\u25BC
#         self.hbox = QHBoxLayout()
#         self.drop_down = QPushButton(u'\u25BC')
#         self.drop_down.setFixedSize(30,30)
#         self.drop_down.setFont(QFont('Arial', 12))
#         self.drop_down.setStyleSheet('''
# background-color:#EBEBEB;border: none;border-style: outset;
# border-width: 1px;
# border-radius: 15px;
# border-color: black;
# color: #6A6A6A  
#             ''')
#         self.drop_down.clicked.connect(self.fun3)

#         self.training = QLabel("Training")
#         self.training.setStyleSheet("color: #6A6A6A")
#         self.training.setFont(QFont('Arial', 15))
#         self.hbox.addWidget(self.drop_down)
#         self.hbox.addWidget(self.training)

#         self.widget_video = QWidget()
#         # self.widget_video.setStyleSheet("background:white")
#         self.widget_video.setFixedHeight(400)

#         self.vbox2_video = QVBoxLayout()
#         self.wvideo1 = QPushButton("Getting Started")
#         self.wvideo1.setFont(QFont('Arial', 15))
#         self.wvideo1.setFixedHeight(60)
#         self.wvideo1.setStyleSheet('''
#         padding-left:10px;
#         background-color:#DADADA;
#         border: none;
#         border-radius: 4px;
#         color: #6A6A6A;
#         Text-align:left
#         ''')
#         self.wvideo2 = QPushButton("Connecting to Data")
#         self.wvideo2.setFont(QFont('Arial', 15))
#         self.wvideo2.setFixedHeight(60)
#         self.wvideo2.setStyleSheet('''
#         padding-left:10px;
#         background-color:#EBEBEB;
#         border: none;
#         border-radius: 4px;
#         color: #6A6A6A;
#         Text-align:left
#         ''')
#         self.wvideo3 = QPushButton('Visual Analytics')
#         self.wvideo3.setFont(QFont('Arial', 15))
#         self.wvideo3.setFixedHeight(60)
#         self.wvideo3.setStyleSheet('''
#         padding-left:10px;
#         background-color:#EBEBEB;
#         border: none;
#         border-radius: 4px;
#         color: #6A6A6A;
#         Text-align:left
#         ''')
#         self.wvideo4 = QPushButton('Understanding tableau')
#         self.wvideo4.setFont(QFont('Arial', 15))
#         self.wvideo4.setFixedHeight(60)
#         self.wvideo4.setStyleSheet('''
#         padding-left:10px;
#         background-color:#EBEBEB;
#         border: none;
#         border-radius: 4px;
#         color: #6A6A6A;
#         Text-align:left
#         ''')

#         self.vbox2_video.addWidget(self.wvideo1)
#         self.vbox2_video.addWidget(self.wvideo2)
#         self.vbox2_video.addWidget(self.wvideo3)
#         self.vbox2_video.addWidget(self.wvideo4)
#         self.vbox2_video.addStretch(stretch=1)

#         self.widget_video.setLayout(self.vbox2_video)
#         self.vbox.addWidget(self.discover_label)
#         self.vbox.addLayout(self.hbox)
#         self.vbox.addWidget(self.widget_video)
#         self.vbox.addStretch(1)
#         self.discover_widget2.setLayout(self.vbox)
    
#     def fun3(self):
#         if(self.drop_down.text()==u'\u25BC'):
#             self.drop_down.setFont(QFont('Arial', 17))
#             self.drop_down.setText(u'\u25B6')
#             self.widget_video.setFixedHeight(0)
#         else:
#             self.drop_down.setFont(QFont('Arial', 12))
#             self.drop_down.setText(u'\u25BC')
#             self.widget_video.setFixedHeight(400)
    
#     def load_data_layout(self):
#         self.load_data_grid_layout = QGridLayout()
#         self.load_data_grid_layout.setContentsMargins(0,0,0,0)
#         self.load_data_grid_layout.setSpacing(0)
#         self.widget1.setLayout(self.load_data_grid_layout)


#         self.load_widget1 = QWidget()
#         self.load_widget1.setStyleSheet("background:white")
#         self.load_widget11 = QWidget()
#         self.load_widget11.setStyleSheet("background:#486DC8")
#         self.load_widget2 = QFrame()
#         self.load_widget2.setStyleSheet("background:#486DC8")
#         self.load_widget3 = QFrame()
#         self.load_widget3.setStyleSheet("background:#486DC8")
#         self.load_widget4 = QFrame()
#         self.load_widget4.setStyleSheet("background:#486DC8")
#         self.load_widget5 = QFrame()
#         self.load_widget5.setStyleSheet("background:#486DC8")

#         self.load_data_grid_layout.setColumnStretch(0, 1)
#         # self.load_data_grid_layout.setColumnStretch(1, 6)

#         self.load_data_grid_layout.setRowStretch(0, 1)
#         self.load_data_grid_layout.setRowStretch(1, 2)
#         self.load_data_grid_layout.setRowStretch(2, 5)
#         self.load_data_grid_layout.setRowStretch(3, 5)
#         self.load_data_grid_layout.setRowStretch(4, 5)
#         self.load_data_grid_layout.setRowStretch(5, 10)
        
        
#         self.load_data_grid_layout.addWidget(self.load_widget1)
#         self.load_data_grid_layout.addWidget(self.load_widget11)
#         self.load_data_grid_layout.addWidget(self.load_widget2)
#         self.load_data_grid_layout.addWidget(self.load_widget3)
#         self.load_data_grid_layout.addWidget(self.load_widget4)
#         self.load_data_grid_layout.addWidget(self.load_widget5)
        

#         self.logo_place()
#         self.search_for_data()
#         self.to_a_file()
#         self.to_a_server()
#         # pass
#     def logo_place(self):

#         self.hbox = QHBoxLayout()
#         self.logo = QLabel()
#         self.logo.setPixmap(QPixmap('logo3.png'))
#         # self.logo.setFixedSize(30,30)
#         self.hbox.addWidget(self.logo)
#         self.load_widget1.setLayout(self.hbox)
#     def search_for_data(self):

#         self.vbox = QVBoxLayout()
#         # self.vbox.setAlignment(Qt.AlignCenter)
#         self.connect_label = QLabel("Connect")
#         self.connect_label.setStyleSheet('color:white;')
#         self.connect_label.setFont(QFont('Arial', 18))
#         # font = QFont()
#         # font.setPointSize(18)
#         # self.connect_label.setFont(font)
#         self.search_for_data = QLabel("Search for Data")
#         self.search_for_data.setStyleSheet('color:#DCDCDC;')
#         self.search_for_data.setFont(QFont('Arial', 13))
#         # self.search_for_data.setFont(font)
#         self.vizpick_server = QLabel("VizPick Server")
#         self.vizpick_server.setStyleSheet('color:white;margin-left:8px')
#         self.vizpick_server.setFont(QFont('Arial', 12))

        
#         self.vbox.addWidget(self.connect_label)
#         self.vbox.addWidget(self.search_for_data)
#         self.vbox.addWidget(self.vizpick_server)
#         self.vbox.addStretch(1)
#         self.load_widget2.setLayout(self.vbox)

#         # pass

#     def to_a_file(self):

#         self.vbox = QVBoxLayout()
#         self.vbox.setAlignment(Qt.AlignTop)
#         self.to_a_file = QLabel("To a File")
#         self.to_a_file.setStyleSheet('color:#DCDCDC;margin-bottom:4px')
#         self.to_a_file.setFont(QFont('Arial', 13))

#         self.m_excel = QPushButton("Microsoft Excel")
#         self.m_excel.setStyleSheet('color:white;margin-left:10px;margin-bottom:4px;border:0;padding:0;Text-align:left')
#         self.m_excel.setFont(QFont('Arial', 12))
        
#         self.csv_file = QLabel("CSV File")
#         self.csv_file.setStyleSheet('color:white;margin-left:10px;margin-bottom:4px;border:0;padding:0;Text-align:left')
#         self.csv_file.setFont(QFont('Arial', 12))
        
#         self.txt_file = QLabel("Text File")
#         self.txt_file.setStyleSheet('color:white;margin-left:10px;margin-bottom:4px;border:0;padding:0;Text-align:left')
#         self.txt_file.setFont(QFont('Arial', 12))

#         self.vbox.addWidget(self.to_a_file)
#         self.vbox.addWidget(self.m_excel)
#         self.vbox.addWidget(self.csv_file)
#         self.vbox.addWidget(self.txt_file)
#         self.vbox.addStretch(1)
#         self.load_widget3.setLayout(self.vbox)

#     def to_a_server(self):

#         self.vbox = QVBoxLayout()
        
#         self.to_a_server = QLabel("To a Server")
#         self.to_a_server.setStyleSheet('color:#DCDCDC;margin-bottom:4px')
#         self.to_a_server.setFont(QFont('Arial', 13))

#         self.upgrade = QPushButton("Upgrade")
#         self.upgrade.setStyleSheet('color:white;margin-left:10px;margin-bottom:4px;border:0;padding:0;Text-align:left')
#         self.upgrade.setFont(QFont('Arial', 12))
        
#         self.vbox.addWidget(self.to_a_server)
#         self.vbox.addWidget(self.upgrade)
#         self.vbox.addStretch(1)
#         self.load_widget4.setLayout(self.vbox)

#     def main_top(self):
#         self.vbox = QVBoxLayout()
#         self.vbox.setAlignment(Qt.AlignCenter)
#         self.c_d_s = QLabel("Current Data Sources")
#         self.c_d_s.setStyleSheet('color:black')
#         self.c_d_s.setFont(QFont('Arial', 20))
        
#         # self.vbox.addStretch(1)
#         self.vbox.addWidget(self.c_d_s)
#         # self.vbox.addStretch(1)
#         self.widget2.setLayout(self.vbox)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 layout - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 1024
        self.height = 768
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setMinimumSize(1024, 768)
        self.showMaximized()
        # self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.createGridLayout()
        
        windowLayout = QVBoxLayout()
        windowLayout.setContentsMargins(0,0,0,0)
        # windowLayout.setSpacing(0)
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        
        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QFrame()
        self.horizontalGroupBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.widgetheading = QWidget()
        self.widgetheading.setStyleSheet("background:blue")

        self.widgetscrollbutton = QWidget()
        self.widgetscrollbutton.setStyleSheet("background:#F8F8F8")

        self.top = QWidget()
        self.top.setStyleSheet("background:pink")

        self.graph = QWidget()
        self.graph.setStyleSheet("background:green")


        
        layout = QGridLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 4)

        
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 2)
        layout.setRowStretch(2, 10)

        
        layout.addWidget(self.widgetheading,0,0,0,0) #1st row 1st column expand to 2nd row 2nd column  ##if we place 0 in expand it will expand full
        layout.addWidget(self.widgetscrollbutton,1,0,2,2)
        layout.addWidget(self.top,1,1,2,1)
        layout.addWidget(self.graph,2,1,2,1)

        self.horizontalGroupBox.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())