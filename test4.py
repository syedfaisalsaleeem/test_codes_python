from PyQt5 import QtGui,QtWidgets,QtCore

def a_function(x):
    print("x : ",x)
act_int = QtWidgets.QAction()
act_str = QtWidgets.QAction()

mapper = QtCore.QSignalMapper()
act_int.triggered.connect(mapper.map)
mapper.setMapping(act_int,1)
act_str.triggered.connect(mapper.map)
mapper.setMapping(act_str,"a_string")
mapper.mapped[str].connect(a_function)

act_int.trigger()
act_str.trigger()