# encoding: utf-8
import sys
from Ui.Ui_MainWindow import UiMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal, QObject
from Slots.BtnEvent import *
from Slots.ClickEvent import *
from Slots.OutputEvent import output
from Utils.Logger import log
"""
处理信号和信号槽函数
"""


class MyWindow(QMainWindow, UiMainWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.initUI(MyWindow)

    #def connect(self):
        #pass
        # 按键槽
        #self.btn_execute.clicked.connect(self.savetestcase)
        #self.btn_savecase.clicked.connect(self.savetestcase)
        #self.btn_addline.clicked.connect(self.btnevent.addline)
        # 事件槽
        #self.comb_selectexcel.currentIndexChanged.connect(self.showexcelsheet)
        #self.btn_load.clicked.connect(self.loadsheet)
        #self.view_sheetlist.itemClicked.connect(self.itemclick)
        #log.trigger.connect(output.printf)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mytest = MyWindow()
    mytest.show()
    sys.exit(app.exec_())