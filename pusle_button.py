from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
class global_():
    color = "white"
    button_start = " "
    value = " "
    layout = " "
    widget = " "
    # pass
class buzzer_run(QThread):
  countChanged = pyqtSignal(str)
  def run(self):
      self.seconds1=0
      self.hours1=0
      self.minutes1=0
      while True:
          global_.button_start.move((global_.widget.width()/2)-80,global_.widget.height()/2)
          print(global_.widget.height())
          if(self.seconds1 == 1):
            self.seconds1 = 0
            global_.color = "white"

            # global_.button_start.setStyleSheet("padding-top:100px;background:white;")
          else:
            self.seconds1 = 1
            global_.color = "black"
            # global_.button_start.setStyleSheet("padding-top:10px;background:red;")
          time.sleep(1)
         # print(seconds1,'seconds1')
          # if(timing_temperature=='close'):
          #         if(self.hours1>0):
          #                 timing_data.timing_data=str(self.hours1)+' hours'
          #         elif(self.hours1>0 and self.minutes1>0):
          #                 timing_data.timing_data=str(self.hours1)+' hrs'+str(self.minutes1)+' min'
          #         elif(self.minutes1>0):
          #                 timing_data.timing_data=str(self.minutes1)+' minutes'
          #         elif(self.minutes1>0 and self.seconds1>0):
          #                 timing_data.timing_data=str(self.minutes1)+' min'+str(self.seconds1)+ ' sec'
          #         elif(seconds1>0):
          #                 timing_data.timing_data=str(self.seconds1)+' seconds'
          #         self.hours1,self.minutes1,self.seconds1=0,0,0
          #         insert_table_temperature()
          #         break
          # if(self.seconds1>=60):
          #     self.minutes1=self.minutes1+1
          #     self.seconds1=0
          #     #print(minutes1,'minutes1')
          #     if(self.minutes1>=59):
          #         self.hours1=self.hours1+1
          #         self.seconds1=0
          #         self.minutes1=0

class BlinkButton(QPushButton):
    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)
        self.default_color = self.getColor()

    def getColor(self):
        return self.palette().color(QPalette.Button)

    def setColor(self, value):
        if value == self.getColor():
            return
        palette = self.palette()
        y = QBrush(value,Qt.SolidPattern)
        palette.setBrush(QPalette.Button,y )
        # palette.setColor(QPalette.Button, value)
        self.setAutoFillBackground(True)
        self.setPalette(palette)

    def reset_color(self):
        self.setColor(self.default_color)

    color = pyqtProperty(QColor, getColor, setColor)


class Widget(QWidget):

    def __init__(self):
        super(Widget, self).__init__()

        self.resize(300,200)
        global_.layout = QVBoxLayout(self)
        # global_.layout.setAlignment(Qt.AlignCenter)
        # hbox = QHBoxLayout()
        # hbox.setContentsMargins(0,0,0,0)
        global_.widget = QWidget()
        # global_.widget.setFixedSize(200, 32)
        # global_.widget.setStyleSheet("background:green;border:0px solid green;padding:0")
        self.button_stop = QPushButton(global_.widget)
        self.button_stop.move(global_.layout.minimumSize().height(),30)
        self.button_stop.setStyleSheet("background:white")
        # hbox.addWidget(self.button_stop)
        # self.tempWidget.setLayout(hbox)
        global_.layout.addWidget(global_.widget)


        global_.button_start = QPushButton("1234",global_.widget)
        font = QFont()
        # set the font size
        font.setPointSize(19)
        #set the font in the label
        # font.setLetterSpacing(QFont.PercentageSpacing,200)
        global_.button_start.setFont(font)
        global_.button_start.move(100,100)
        # global_.button_start.setFont(QFont("Arial",22))
        global_.button_start.setStyleSheet("background:white;border:2px solid red;padding:0")
        # global_.layout.addWidget(global_.button_start)
        def onCountChanged(value):
            if(value=="stop"):
                x1.terminate()
        x1 = buzzer_run()
        x1.countChanged.connect(onCountChanged)
        x1.start()
        self.button_start = QPushButton("Use DataSource", self)
        self.effect = QGraphicsDropShadowEffect(global_.button_start)
        self.effect.setOffset(0, 0)
        self.effect.setColor(QColor(0,255,0))
        self.effect.setBlurRadius(50)
        # self.effect = QGraphicsOpacityEffect()
        # self.effect.setOpacity(1)
        global_.button_start.setGraphicsEffect(self.effect)
        self.animation = QPropertyAnimation(self.effect,b'blurRadius')
        self.animation.setDuration(1000)

        
        self.animation.setLoopCount(-1)
        self.animation.setStartValue(10);
        self.animation.setEndValue(50);
        # self.animation.setStartValue(self.button_stop.default_color)
        # self.animation.setEndValue(self.button_stop.default_color)
        # self.animation.setStartValue(0);
        # self.animation.setEndValue(1000);
        self.animation.setEasingCurve(QEasingCurve.InOutCubic);
        # self.animation.setStartValue(QColor(0,255,0))
        # self.animation.setEndValue(QColor(0,200,0))
        # self.animation.setKeyValueAt(0.1, QColor(0,255,0))
        # self.animation.setKeyValueAt(0.15,QColor(0,200,0))
        # self.animation.setKeyValueAt(0.3, QColor(0,215,0))
        # self.animation.setKeyValueAt(0.5, QColor(0,225,0))
        # self.animation.setKeyValueAt(0.75,QColor(0,245,0))
        
        self.animation.start()
        # self.button_start.clicked.connect(self.animation.start)
        # self.button_stop.clicked.connect(self.stop)

    def stop(self):
        self.animation.stop()
        self.button_stop.reset_color()

if __name__ == "__main__":
    app = QApplication([])
    w = Widget()
    w.show()
    app.exec_()