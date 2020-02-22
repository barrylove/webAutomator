import datetime
from PyQt5.QtCore import pyqtSignal, QThread


class Logger(QThread):
    trigger = pyqtSignal(str)

    def logger(self, level, logstr):
        date = datetime.datetime.now()
        logmessage = r'{} - {} - {}'.format(date, level, logstr)
        self.trigger.emit(logmessage)


log = Logger()

if __name__ == '__main__':
    log.logger('info', 'logstr')