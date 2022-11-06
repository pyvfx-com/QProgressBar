from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class moWidget(QWidget):
    def __int__(self, parent=None):
        super(moWidget, self).__int__(parent)
        self.parent = parent

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.parent.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.parent.move(event.globalPos() - self.dragPosition)
            event.accept()


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 206)
        Form.setMinimumSize(QSize(400, 206))
        Form.setMaximumSize(QSize(400, 206))
        Form.setWindowFlags(Qt.FramelessWindowHint)
        Form.setAttribute(Qt.WA_TranslucentBackground)

        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = moWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.allnode = QPushButton(self.frame_2)
        self.allnode.setObjectName(u"allnode")

        self.horizontalLayout.addWidget(self.allnode)

        self.selnode = QPushButton(self.frame_2)
        self.selnode.setObjectName(u"selnode")

        self.horizontalLayout.addWidget(self.selnode)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.chenge_tilecolor = QPushButton(self.frame_2)
        self.chenge_tilecolor.setObjectName(u"chenge_tilecolor")

        self.verticalLayout_2.addWidget(self.chenge_tilecolor)

        self.verticalLayout.addWidget(self.frame_2)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Done", None))
        self.allnode.setText(QCoreApplication.translate("Form", u"All Nodes", None))
        self.selnode.setText(QCoreApplication.translate("Form", u"Selected Node", None))
        self.chenge_tilecolor.setText(QCoreApplication.translate("Form", u"Change Color", None))
    # retranslateUi
