import sys, os
from PyQt5.QtWidgets import QApplication, QLabel, QListWidget, QHBoxLayout,\
    QPushButton, QWidget, QTableWidget, QVBoxLayout, QHeaderView, QMessageBox,\
    QComboBox, QInputDialog, QLineEdit, QTextBrowser, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from Utils.ScriptExecute import *
from Utils.GetFuncName import *
from collections import OrderedDict
from Utils.EditExcel import *
from Utils.Logger import log


class UiMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

    def retanslateUi(self):
        