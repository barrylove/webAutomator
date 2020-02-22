# encoding: utf-8
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QListWidget, QHBoxLayout,\
    QPushButton, QWidget, QTableWidget, QVBoxLayout, QHeaderView, QComboBox, QTextBrowser
from PyQt5.QtCore import Qt, QMetaObject
from Config.varconfig import *
"""
主界面的UI
"""


class UiMainWindow(object):
    def initUI(self, MainWindow):
        """
        生成各个控件
        :return:
        """
        # 主体大小
        self.setGeometry(200, 200, 1000, 650)
        self.setWindowTitle('网页自动化脚本')
        # Label控件
        self.label_stepstable = QLabel('操作步骤顺序')
        self.label_sheetlist = QLabel('测试用例')
        self.label_logbrowser = QLabel('运行日志')
        # 按钮控件
        self.btn_execute = QPushButton('执行')
        self.btn_savecase = QPushButton('保存用例->')
        self.btn_addline = QPushButton('增加一行')
        self.btn_load = QPushButton('<-读取用例')
        # 表格控件
        self.view_stepstable = QTableWidget()   #步骤编辑框
        self.view_sheetlist = QListWidget()     #用例选择框
        self.view_logbrowser = QTextBrowser()   #日志展示框
        # 下拉框控件
        self.comb_selectexcel = QComboBox()          #用例集选择下拉框
        # view_stepstable设置
        self.view_stepstable.setColumnCount(COLUNM_NUMBER)
        self.view_stepstable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # 不显示水平滚动条
        self.view_stepstable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)   # 自适应宽度
        self.view_stepstable.setHorizontalHeaderLabels(COLUNM_NAMES) # 列名
        # 布局框架
        self.box_viewlabels = QHBoxLayout()  # label布局
        self.box_viewlabels.addWidget(self.label_stepstable)
        self.box_viewlabels.addStretch(1)
        self.box_viewlabels.addWidget(self.label_sheetlist)
        self.box_views = QHBoxLayout()   # 展示框布局
        self.box_steps = QVBoxLayout()  # 步骤框布局
        self.box_steps.addWidget(self.view_stepstable)
        self.box_btnsave = QVBoxLayout()  # 保存读取按钮布局
        self.box_btnsave.addWidget(self.btn_savecase)
        self.box_btnsave.addWidget(self.btn_load)
        self.box_cases = QVBoxLayout()  # 读取用例布局
        self.box_cases.addWidget(self.comb_selectexcel, stretch=1)
        self.box_cases.addWidget(self.view_sheetlist, stretch=2)
        self.box_views.addLayout(self.box_steps, stretch=8)
        self.box_views.addLayout(self.box_btnsave, stretch=1)
        self.box_views.addLayout(self.box_cases, stretch=2)
        self.box_loglabel = QHBoxLayout()   # 日志labels框布局
        self.box_loglabel.addWidget(self.label_logbrowser)
        self.box_loglabel.addStretch(1)
        self.box_logview = QHBoxLayout()    # 日志展示框
        self.box_logview.addWidget(self.view_logbrowser)
        self.box_executebtns = QHBoxLayout()    # 执行按钮布局
        self.box_executebtns.addStretch(6)
        self.box_executebtns.addWidget(self.btn_addline)
        self.box_executebtns.addWidget(self.btn_execute)
        self.box_executebtns.addStretch(3)
        #布局
        vbox = QVBoxLayout()    #最外围垂直框
        vbox.addLayout(self.box_viewlabels)
        vbox.addLayout(self.box_views)
        vbox.addLayout(self.box_loglabel)
        vbox.addLayout(self.box_logview)
        vbox.addLayout(self.box_executebtns)
        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mytest = UiMainWindow()
    mytest.show()
    sys.exit(app.exec_())






