import sys
import os
import time

from PySide2.QtWidgets import *
from PySide2 import QtCore
from datetime import datetime
from ui.progressbar import Ui_Form

date = datetime.now()
month = date.strftime("%B")
year = date.strftime("%Y")
username = os.getlogin()


class progress_ui(Ui_Form, QWidget):
    def __init__(self):
        super(progress_ui, self).__init__()
        self.setupUi(self)

        self.Qprogress_bar = QtCore.QThread()
        self.Qprogress_bar.run = self.test_progress

        self.Qprogress_bar.start()

    def test_progress(self):
        binlist = os.listdir('/usr/bin/')
        for count, a in enumerate(binlist):
            time.sleep(.01)
            # percentage = len(binlist) / (count + 1) * 100
            percentage = (round(100 * (count + 1) / len(binlist)))
            self.progressBar.setValue(percentage)  # count * 100 / 100
            print(percentage)


def _show():
    _ui = progress_ui()
    _ui.show()


# For widgets
if __name__ == '__main__':
    widgets = progress_ui()
    widgets.show()

