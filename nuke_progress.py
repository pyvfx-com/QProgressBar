import sys
sys.path.append("/home/rion/Github")

import time
import os
from PySide2.QtWidgets import *
from PySide2 import QtCore


from QProgressBar.ui.progressbar import Ui_Form



class progress_ui(Ui_Form, QWidget):
    def __init__(self):
        super(progress_ui, self).__init__()
        self.setupUi(self)
        self.progressBar.setValue(0)

        self.Qprogress_bar = QtCore.QThread()
        self.Qprogress_bar.run = self.test_progress
        self.Qprogress_bar.daemon = True

        self.chenge_tilecolor.clicked.connect(self.Qprogress_bar.start)

    def test_progress(self):
        Nodes = nuke.selectedNodes()
        if not Nodes:
            Nodes = nuke.allNodes()

        for count, a in enumerate(Nodes):
            a['tile_color'].setValue(1145324799)
            self.label.setText(a.name())
            time.sleep(.01)
            percentage = (round(100 * (count + 1) / len(Nodes)))
            self.progressBar.setValue(percentage)


def _show():
    _ui = progress_ui()
    _ui.show()



_show()


