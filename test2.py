import sys
import random
from functools import partial
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap,QPainter,QFont,QCursor,QMovie,QTextCursor,QColor,QPen
from PyQt5.QtCore import QThread, pyqtSignal,QTimer,QTime,Qt,QRect
from PyQt5.QtWidgets import (QPlainTextEdit,QHeaderView,QScroller,QAbstractItemView,QComboBox,QGraphicsDropShadowEffect,QWidget,QMainWindow,QFrame,
  QApplication, QDialog,QProgressBar, QPushButton,QMdiSubWindow,QTreeWidget,QLabel,QLineEdit,QTreeWidgetItem,QMdiArea,QGraphicsView)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import (
    QHeaderView,
    QWidget,
    QLineEdit,
    QApplication,
    QTableView,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
    QPushButton,
    QCheckBox,
    QMessageBox,
)
import pprint

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.btn = QPushButton()
        self.btn.setText("=")
        self.btn.setFixedWidth(20)

        self.linee = QLineEdit()
        self.linee.setPlaceholderText("Filter")

        lay = QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)
        lay.addWidget(self.btn)
        lay.addWidget(self.linee)

class FilterHeader(QHeaderView):
    filterActivated = pyqtSignal()

    def __init__(self, parent):
        super().__init__(Qt.Horizontal, parent)
        self._editors = []
        self.list=[]
        self.list1=[]
        self.list2=[]
        self.label_dct = {}
        self._padding = 0
        self.list_type=['number','abc','date','number','abc','number','date']
        self.setStretchLastSection(True)
        # self.setResizeMode(QHeaderView.Stretch)
        self.setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.setSortIndicatorShown(False)
        self.sectionResized.connect(self.adjustPositions)
        parent.horizontalScrollBar().valueChanged.connect(self.adjustPositions)

    def setFilterBoxes(self, count):
        while self._editors:
            editor = self._editors.pop()
            editor.deleteLater()
        for index in range(count):
            print(index)
            editor = self.create_editor(self.parent(), index,self.list_type[index])
            self._editors.append(editor)
        self.adjustPositions()

    def create_editor(self, parent, index,type):
        layout = QGridLayout()
        mapper = QSignalMapper(self)
        mapper1 = QSignalMapper(self)
        mapper2 = QSignalMapper(self)
        self.funlist=QListWidget()
        editor = QWidget(parent)
        editor.setLayout(layout)
        editor.setGeometry(0, 0, 0, 100)
        # editor.setStyleSheet("background-color:white;")
        # editor.connect(QPushButton)
        editor.setStyleSheet("""
            QWidget{
            background-color:white;
            }
            
            QPushButton[Test=true] {
                border: 2px solid #8f8f91;
                border-radius: 6px;
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #f6f7fa, stop: 1 #dadbde);
                min-width: 80px;
            }

            QPushButton#StyledButton[Test=true] {
                color: #F00;
                background-color: #000;
            }
                           """
                           )
        editor.show()
        self.d_off = QPushButton('#')
        self.d_off.setProperty('Test', True)
        self.d_off.setCheckable(True)
        self.d_off.resize(1024, 768)
        self.list.append(self.d_off)
        self.d_off.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        itemN = QListWidgetItem()
        # Create widget
        widget = QWidget()
        widgetText = QLabel("I love PyQt!")
        widgetButton = QPushButton("Push Me")
        widgetLayout = QHBoxLayout()
        widgetLayout.addWidget(widgetText)
        widgetLayout.addWidget(widgetButton)
        widgetLayout.addStretch()

        widgetLayout.setSizeConstraint(QLayout.SetFixedSize)
        widget.setLayout(widgetLayout)
        itemN.setSizeHint(widget.sizeHint())
        self.funlist.addItem(itemN)
        self.funlist.setItemWidget(itemN, widget)
        # pprint.pprint(vars(QPushButton))
        # pprint(pprintself.d_off
        self.d_off.clicked.connect(mapper.map)
        # QListWidgetItem(self.d_off)
        # mylistWidget.addItem(self.d_off)
        mapper.setMapping(self.d_off,index)
        mapper.mapped[int].connect(self.a_function)
        # self.d_off.clicked.connect(lambda: self.toggle(self.d_off),mapper)
        # self.d_off.setStyleSheet("QPushButton{background-color:#7B7B7B; color: white;border: none;border-style: outset;border-width:1px;border-radius: 1px;border-color: black;} QPushButton:checked { background-color:#4299ff;color:white; }")
        self.d_off.setChecked(True)
        
        self.d_50 = QPushButton('ABC', editor)
        self.d_50 .setProperty('Test', True)
        self.d_50.setCheckable(True)
        self.d_50.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.d_50.clicked.connect(mapper1.map)
        # QListWidgetItem(self.d_off)
        # mylistWidget.addItem(self.d_off)
        mapper1.setMapping(self.d_50,index)
        mapper1.mapped[int].connect(self.b_function)
        self.list1.append(self.d_50)
        # self.d_50.clicked.connect(lambda: self.toggle(self.d_50))
        # self.d_50.clicked.connect(self.creating_function)
        # self.d_50.setStyleSheet("QPushButton{background-color:#7B7B7B; color: white;border: none;border-style: outset;border-width:1px;border-radius: 1px;border-color: black;} QPushButton:checked { background-color:#4299ff;color:white; }")
        # pybutton.setChecked(True)
        self.d_100 = QPushButton('DATE', editor)
        self.d_100 .setProperty('Test', True)
        self.d_100.setCheckable(True)
        self.d_100.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.d_100.clicked.connect(mapper2.map)
        # self.d_100.clicked.connect(lambda d100:self.d_100_on(d100))
        # self.d_100.setStyleSheet("QPushButton{background-color:#7B7B7B; color: white;border: none;border-style: outset;border-width:1px;border-radius: 1px;border-color: black;} QPushButton:checked { background-color:#4299ff;color:white; }")
        self.list2.append(self.d_100)
        mapper2.setMapping(self.d_100,index)
        mapper2.mapped[int].connect(self.c_function)
        
        # self.label_dct[assign_button] = worker_label
        layout.addWidget(self.d_off)
        layout.addWidget(self.d_50)
        layout.addWidget(self.d_100)
        self.check(type,index)
        # editor=QPushButton('Click me', parent)
        # editor.resize(400,400)
        # pybutton = QPushButton('Click me', editor)
        # # pybutton.clicked.connect(self.clickMethod)
        # pybutton.resize(100,32)
        # pybutton1 = QPushButton('Click me', editor)
        # # pybutton.clicked.connect(self.clickMethod)
        # pybutton1.resize(100,32)
        # pybutton.move(0, 0) 
        # if index == 1:  # Empty
        #     editor = QWidget()
        # elif index == 2:  # Number filter (>|=|<)
        #     editor = Widget(parent)
        #     editor.linee.returnPressed.connect(self.filterActivated)
        #     editor.btn.clicked.connect(self.changebuttonsymbol)
        # elif index == 3:
        #     editor = QComboBox(parent)
        #     editor.addItems(["", "Combo", "One", "Two", "Three"])
        #     editor.currentIndexChanged.connect(self.filterActivated)
        # elif index == 4:
        # editor = QPushButton(parent)
        # editor.clicked.connect(self.filterActivated)
        # editor.setText("Button")
        # editor = QPushButton(parent)
        # editor.clicked.connect(self.filterActivated)
        # editor.setText("Button")
        # editor = QPushButton(parent)
        # editor.clicked.connect(self.filterActivated)
        # editor.setText("Button")
            # editor = QPushButton(parent)
            # editor.clicked.connect(self.filterActivated)
            # editor.setText("Button1")
            # editor1 = QPushButton(parent)
            # editor1.clicked.connect(self.filterActivated)
            # editor1.setText("Button")
        # elif index == 5:
        #     editor = QCheckBox(parent)
        #     editor.clicked.connect(self.filterActivated)
        #     editor.setTristate(True)
        #     editor.setCheckState(Qt.Checked)
        #     editor.setText("CheckBox")
        # else:
        #     editor = QLineEdit(parent)
        #     editor.setPlaceholderText("Filter")
        #     editor.returnPressed.connect(self.filterActivated)
        return editor
    def check(self,type,x):
        print("pass",type)
        if(type=="number"):
            self.list[x].setStyleSheet('background-color:#4299ff;color:white;')
        elif(type=="abc"):
            self.list1[x].setStyleSheet('background-color:#4299ff;color:white;')
        else:
            self.list2[x].setStyleSheet('background-color:#4299ff;color:white;')

    def a_function(self,x):

        print("x : ",x)
        print(self.d_off)
        # pprint.pprint(vars(QListWidget))
        print(self.funlist,self.list)
        self.list[x].setStyleSheet('background-color:#4299ff;color:white;')
        self.list1[x].setStyleSheet('background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #dadbde);')
        self.list2[x].setStyleSheet('background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #dadbde);')
        # if(x==0):
        #     self.list[0].setStyleSheet('background-color:green')

    def b_function(self,x):

        print("x : ",x)
        print(self.d_off)
        # pprint.pprint(vars(QListWidget))
        print(self.funlist,self.list)
        # self.list[x].setStyleSheet('background-color:red')
        self.list1[x].setStyleSheet('background-color:#4299ff;color:white;')
        self.list[x].setStyleSheet('background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #dadbde);')
        self.list2[x].setStyleSheet('background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #dadbde);')
        # if(x==0):
        #     self.list[0].setStyleSheet('background-color:red')
    def c_function(self,x):

        print("x : ",x)
        print(self.d_off)
        # pprint.pprint(vars(QListWidget))
        print(self.funlist,self.list)
        # self.list[x].setStyleSheet('background-color:red')
        self.list2[x].setStyleSheet('background-color:#4299ff;color:white;')
        self.list1[x].setStyleSheet('background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #dadbde);')
        self.list[x].setStyleSheet('background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #dadbde);')
        # if(x==0):
        #     self.list[0].setStyleSheet('background-color:red')
    def toggle(self, widget):
        # Query the attribute
        isTest = widget.property("Test")
        widget.setProperty('Test', not isTest)

        # Update the style
        widget.setStyle(widget.style())
    def creating_function(self):
        nbtn = self.sender()
        pprint.pprint(vars(nbtn))
        print(nbtn.text())
        if(nbtn.text()=="ABC"):
            self.d_off.setEnabled(True)
            self.d_50.setEnabled(False)
            self.d_100.setEnabled(True)
            
            self.d_off.setCheckable(False)
            self.d_off.setEnabled(False)
            self.d_off.setEnabled(True)
            self.d_off.setCheckable(True)

            self.d_100.setCheckable(False)
            self.d_100.setEnabled(False)
            self.d_100.setEnabled(True)
            self.d_100.setCheckable(True)

    def d_50_on(self,d50):
        #self.d_50.setCheckable(False)
        # if(d50==True):
        #     self.d50=1
        # elif(d50==False):
        #     self.d50=0
        nbtn = self.sender()
        print("50",nbtn.text())
        self.d_off.setEnabled(True)
        self.d_50.setEnabled(False)
        self.d_100.setEnabled(True)
        
        self.d_off.setCheckable(False)
        self.d_off.setEnabled(False)
        self.d_off.setEnabled(True)
        self.d_off.setCheckable(True)

        self.d_100.setCheckable(False)
        self.d_100.setEnabled(False)
        self.d_100.setEnabled(True)
        self.d_100.setCheckable(True)


    def d_off_on(self,doff):
        # if(doff==True):
        #     self.doff=1
        # elif(doff==False):
        #     self.doff=0
        print("off")
        self.d_off.setEnabled(False)
        self.d_50.setEnabled(True)
        self.d_100.setEnabled(True)

        self.d_50.setCheckable(False)
        self.d_50.setEnabled(False)
        self.d_50.setEnabled(True)
        self.d_50.setCheckable(True)

        self.d_100.setCheckable(False)
        self.d_100.setEnabled(False)
        self.d_100.setEnabled(True)
        self.d_100.setCheckable(True)


    def d_100_on(self,d100):
        # if(d100==True):
        #     self.d100=1
        # elif(doff==False):
        #     self.d100=0
        print("100")
        #self.d_off.setEnabled(False)
        self.d_100.setEnabled(False)
        self.d_50.setEnabled(True)
        self.d_off.setEnabled(True)

        self.d_50.setCheckable(False)
        self.d_50.setEnabled(False)
        self.d_50.setEnabled(True)
        self.d_50.setCheckable(True)

        self.d_off.setCheckable(False)
        self.d_off.setEnabled(False)
        self.d_off.setEnabled(True)
        self.d_off.setCheckable(True)

    

    def sizeHint(self):
        size = super().sizeHint()
        if self._editors:
            height = self._editors[0].sizeHint().height()
            size.setHeight(size.height() + height + self._padding)
        return size

    def updateGeometries(self):
        if self._editors:
            height = self._editors[0].sizeHint().height()
            self.setViewportMargins(0, 0, 0, height + self._padding)
        else:
            self.setViewportMargins(0, 0, 0, 0)
        super().updateGeometries()
        self.adjustPositions()

    def adjustPositions(self):
        for index, editor in enumerate(self._editors):
            if not isinstance(editor, QWidget):
                continue
            height = editor.sizeHint().height()+22
            compensate_y = 0
            compensate_x = 0
            if type(editor) is QComboBox:
                compensate_y = +2
            elif type(editor) in (QWidget, Widget):
                compensate_y = -1
            elif type(editor) is QPushButton:
                compensate_y = -1
            elif type(editor) is QCheckBox:
                compensate_y = 4
                compensate_x = 4
            editor.move(
                self.sectionPosition(index) - self.offset() + 1 + compensate_x,
                26+ compensate_y,
            )
            editor.resize(self.sectionSize(index), height+5)

    def filterText(self, index):
        for editor in self._editors:
            if hasattr(editor, "text") and callable(editor.text):
                return editor.text()
        return ""

    def setFilterText(self, index, text):
        for editor in self._editors:
            if hasattr(editor, "setText") and callable(editor.setText):
                editor.setText(text)

    def clearFilters(self):
        for editor in self._editors:
            editor.clear()

    def changebuttonsymbol(self):
        nbtn = self.sender()
        if nbtn.text() == "=":
            nbtn.setText(">")
        elif nbtn.text() == ">":
            nbtn.setText("<")
        else:
            nbtn.setText("=")

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.filter_button = QPushButton("Filter")
        self.filter_button.setCheckable(True)
        self.filter_button.setChecked(True)
        self.filter_button.clicked.connect(self.on_button_clicked)
        self.view = QTableView()
        self.view.setGeometry(100,100,500,500)
        self.view.horizontalHeader().setStretchLastSection(True)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.filter_button)

        layout = QVBoxLayout(self)
        layout.addLayout(button_layout)
        layout.addWidget(self.view)

        header = FilterHeader(self.view)
        self.view.setHorizontalHeader(header)
        self.view.verticalHeader().setVisible(False)
        #model = QStandardItemModel(self.view)
        model = QStandardItemModel(5, 7, self.view)
        for i in range(5):
            for j in range(7):
                item = QStandardItem(str(i+j))
                model.setItem(i, j, item)
        model.setHorizontalHeaderLabels("One Two Three Four Five Six Seven".split())
        self.view.setModel(model)
        header.setFilterBoxes(model.columnCount())
        header.filterActivated.connect(self.handleFilterActivated)

    def handleFilterActivated(self):
        header = self.view.horizontalHeader()
        # print()
        for index in range(header.count()):
            if index != 4:
                print(index, header.filterText(index))
            else:
                print("Button")

    def on_button_clicked(self):
        if self.filter_button.isChecked():
            QMessageBox.information(None, "", "Now I want the row with filters below the QHeaderView to appear again.")
        else:
            QMessageBox.information(None, "", "Now I want the row with filters below the QHeaderView to disappear.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    #window.setGeometry(800, 100, 600, 300)
    window.resize(1024, 768)
    window.show()
    sys.exit(app.exec_())