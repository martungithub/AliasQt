from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer,QTime
import time
from PyQt5.QtWidgets import QWidget, QSizePolicy, QLCDNumber, QFrame, QVBoxLayout

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(623, 538)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.word1 = QtWidgets.QPushButton(self.centralwidget)
        self.word1.setGeometry(QtCore.QRect(160, 90, 311, 61))
        font = QtGui.QFont()
        font.setFamily("GHEA Grapalat")
        font.setPointSize(12)
        font.setItalic(True)
        self.word1.setFont(font)
        self.word1.setObjectName("word1")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(190, 10, 151, 61))
        font = QtGui.QFont()
        font.setFamily("GHEA Grapalat")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumber.setLineWidth(1)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.teamname = QtWidgets.QLabel(self.centralwidget)
        self.teamname.setGeometry(QtCore.QRect(20, 10, 251, 61))
        font = QtGui.QFont()
        font.setFamily("GHEA Grapalat")
        font.setPointSize(20)
        font.setItalic(True)
        self.teamname.setFont(font)
        self.teamname.setObjectName("teamname")
        self.score = QtWidgets.QLabel(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(410, 10, 211, 61))
        font = QtGui.QFont()
        font.setFamily("GHEA Grapalat")
        font.setPointSize(20)
        font.setItalic(True)
        self.score.setFont(font)
        self.score.setObjectName("score")
        self.word2 = QtWidgets.QPushButton(self.centralwidget)
        self.word2.setGeometry(QtCore.QRect(160, 160, 311, 61))
        font = QtGui.QFont()
        font.setFamily("GHEA Grapalat")
        font.setPointSize(12)
        font.setItalic(True)
        self.word2.setFont(font)
        self.word2.setObjectName("word2")
        self.word4 = QtWidgets.QPushButton(self.centralwidget)
        self.word4.setGeometry(QtCore.QRect(160, 300, 311, 61))
        font = QtGui.QFont()
        font.setFamily("GHEA Grapalat")
        font.setPointSize(12)
        font.setItalic(True)
        self.word4.setFont(font)
        self.word4.setObjectName("word4")
        self.word3 = QtWidgets.QPushButton(self.centralwidget)
        self.word3.setGeometry(QtCore.QRect(160, 230, 311, 61))
        font = QtGui.QFont()
        font.setFamily("GHEA Grapalat")
        font.setPointSize(12)
        font.setItalic(True)
        self.word3.setFont(font)
        self.word3.setObjectName("word3")
        self.word5 = QtWidgets.QPushButton(self.centralwidget)
        self.word5.setGeometry(QtCore.QRect(160, 370, 311, 61))
        font = QtGui.QFont()
        font.setFamily("GHEA Grapalat")
        font.setPointSize(12)
        font.setItalic(True)
        self.word5.setFont(font)
        self.word5.setObjectName("word5")
        self.points = QtWidgets.QLabel(self.centralwidget)
        self.points.setGeometry(QtCore.QRect(280, 450, 81, 21))
        font = QtGui.QFont()
        font.setFamily("GHEA Grapalat")
        font.setPointSize(11)
        font.setItalic(True)
        self.points.setFont(font)
        self.points.setObjectName("points")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 623, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        print(self.points.text())
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.Time)
        self.teams = []
        self.scores = []
        self.clickcount = 0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def on_click(self,name):

        self.clickcount += 1


    def Start(self):

        self.timer.start(1000)

    def Time(self):

        l = self.lcdNumber.value()
        s = l
        curr_score = 0
        winning_score = int(self.points.text())

        if curr_score <= winning_score:
            curr_score = 0
            if s > 0:
                s -= 0.5
            else:
                self.timer.stop()


        self.lcdNumber.display(s)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.word1.setText(_translate("MainWindow", "PushButton"))
        self.teamname.setText(_translate("MainWindow", "Teamname"))
        self.score.setText(_translate("MainWindow", f"Score"))
        self.word2.setText(_translate("MainWindow", "PushButton"))
        self.word4.setText(_translate("MainWindow", "PushButton"))
        self.word3.setText(_translate("MainWindow", "PushButton"))
        self.word5.setText(_translate("MainWindow", "PushButton"))
        self.timer.timeout.connect(self.Time)
        self.word1.clicked.connect(self.on_click)
        self.word2.clicked.connect(self.on_click)
        self.word3.clicked.connect(self.on_click)
        self.word4.clicked.connect(self.on_click)
        self.word5.clicked.connect(self.on_click)
