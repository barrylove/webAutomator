from PyQt5.QtWidgets import QApplication
from Ui.Ui_MainWindow import UiMainWindow

class Output(UiMainWindow):
    def __init(self):
        pass

    # 打印到日志
    def printf(self, msg):
        self.view_logbrowser.append(msg)  # 在指定的区域显示提示信息
        self.cursor = self.view_logbrowser.textCursor()
        self.view_logbrowser.moveCursor(self.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QApplication.processEvents()  # 一定加上这个功能，不然有卡顿

output = Output()