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
        self._padding = 44
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
            editor = self.create_editor(self.parent(), index)
            self._editors.append(editor)
        self.adjustPositions()

    def create_editor(self, parent, index):
        if index == 1:  # Empty
            editor = QWidget()
        elif index == 2:  # Number filter (>|=|<)
            editor = Widget(parent)
            editor.linee.returnPressed.connect(self.filterActivated)
            editor.btn.clicked.connect(self.changebuttonsymbol)
        elif index == 3:
            editor = QComboBox(parent)
            editor.addItems(["", "Combo", "One", "Two", "Three"])
            editor.currentIndexChanged.connect(self.filterActivated)
        elif index == 4:
            editor = QPushButton(parent)
            editor.clicked.connect(self.filterActivated)
            editor.setText("Button")
            # editor = QPushButton(parent)
            # editor.clicked.connect(self.filterActivated)
            # editor.setText("Button1")
            # editor1 = QPushButton(parent)
            # editor1.clicked.connect(self.filterActivated)
            # editor1.setText("Button")
        elif index == 5:
            editor = QCheckBox(parent)
            editor.clicked.connect(self.filterActivated)
            editor.setTristate(True)
            editor.setCheckState(Qt.Checked)
            editor.setText("CheckBox")
        else:
            editor = QLineEdit(parent)
            editor.setPlaceholderText("Filter")
            editor.returnPressed.connect(self.filterActivated)
        return editor

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
            height = editor.sizeHint().height()
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
                height + (self._padding // 2) + 2 + compensate_y,
            )
            editor.resize(self.sectionSize(index), height)

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
        print()
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
    window.resize(950, 220)
    window.show()
    sys.exit(app.exec_())