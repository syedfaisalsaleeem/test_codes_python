from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self._setupscrollbar()

    def _setupscrollbar(self):
        self.v = QVBoxLayout(self)
        self.scrollArea = QScrollArea()

        self.widget = QWidget()
        # self.widget.setFixedSize(200, 300)
        # self.widget.setStyleSheet("background:red")
        self.vbox = QVBoxLayout()
        self.widget1 = QWidget()
        self.widget1.setFixedSize(200, 300)
        self.widget1.setStyleSheet("background:red")
        self.vbox.addWidget(self.widget1)

        self.widget.setLayout(self.vbox)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widget)
        self.v.addWidget(self.scrollArea)
        self.setLayout(self.v)
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.setGeometry(800, 100, 600, 300)
    # window.resize(1024, 768)
    window.show()
    sys.exit(app.exec_())