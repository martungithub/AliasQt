from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(637, 563)
        Frame.styleSheet()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Desktop/Books/alias-logo-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Frame.setWindowIcon(icon)
        Frame.setWindowOpacity(0.0)
        Frame.setToolTipDuration(-1)
        self.play = QtWidgets.QPushButton(Frame)
        self.play.setGeometry(QtCore.QRect(210, 110, 231, 71))
        self.play.setObjectName("play")
        self.rules = QtWidgets.QPushButton(Frame)
        self.rules.setGeometry(QtCore.QRect(210, 230, 231, 71))
        self.rules.setObjectName("rules")
        self.add_words = QtWidgets.QPushButton(Frame)
        self.add_words.setGeometry(QtCore.QRect(210, 350, 231, 71))
        self.add_words.setObjectName("add_words")
        self.add_button = QtWidgets.QPushButton(Frame)
        self.add_button.setGeometry(QtCore.QRect(280, 300, 80, 40))
        self.add_button.setObjectName("add_button")
        self.label = QtWidgets.QLabel(Frame)
        self.lineEntry = QLineEdit(Frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 611, 531))
        self.label.setObjectName("label")
        self.message_lab = QtWidgets.QLabel(Frame)
        self.message_lab.setGeometry(QtCore.QRect(10, 10, 611, 531))
        self.message_lab.setObjectName("message_lab")
        self.label.setScaledContents(True)
        self.message_lab.setText("You can add as many word as you want!")
        self.message_lab.move(130, 180)
        self.message_lab.resize(450, 50)
        self.message_lab.setFont(QFont('Comic Sans Serif', 14))
        self.message_lab.setStyleSheet("color: yellow")
        self.rules.raise_()
        self.play.raise_()
        self.add_words.raise_()
        self.label.raise_()
        self.back = QtWidgets.QPushButton(Frame)
        self.back.setGeometry(QtCore.QRect(10, 10, 100, 50))
        self.back.setObjectName("back")
        self.back.hide()
        my_qframe = Frame
        my_qframe.setStyleSheet(".QFrame { background-color:purple; }")
        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)
        self.lineEntry.move(170, 250)
        self.lineEntry.resize(300, 40)
        self.lineEntry.hide()
        self.add_button.hide()
        self.message_lab.hide()
        self.w = None

    def back_to_main(self):
        self.rules.show()
        self.play.show()
        self.add_words.show()
        self.back.hide()
        self.label.hide()
        self.lineEntry.hide()
        self.add_button.hide()
        self.message_lab.hide()

    def changelabeltext(self):
        # changing the text of label after button get clicked
        # Hiding pushbutton from the main window
        # after button get clicked.
        self.rules.hide()
        self.play.hide()
        self.add_words.hide()
        self.back.show()

        pixmap = QPixmap('rules.png')
        self.label.setPixmap(pixmap)
        self.label.show()

    def words(self):
        self.rules.hide()
        self.play.hide()
        self.add_words.hide()
        self.back.show()
        self.lineEntry.show()
        self.add_button.show()
        self.message_lab.show()

    def insert_word(self):
        entry_text = self.lineEntry.text()
        f = open("words.txt", "r")
        if any(char.isdigit() for char in entry_text):
            self.message_lab.setText("Your word contains numbers. Input new one.")
            self.lineEntry.setText("")
        elif entry_text == "" or entry_text == " ":
            self.message_lab.setText("The line is empty. Input new word, please.")
            self.lineEntry.setText("")

        elif entry_text in f.read():
            self.message_lab.setText("This word is already exists in the database.")
            f.close()
        else:
            f = open("words.txt", "a")
            f.write(f"{entry_text}\n")
            f.close()
            self.lineEntry.setText("")
            self.message_lab.setText("The word has been inserted. One more?")


    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Alias"))
        self.play.setText(_translate("Frame", "Play"))
        self.rules.setText(_translate("Frame", "Rules"))
        self.add_words.setText(_translate("Frame", "Add words"))
        self.back.setText(_translate("Frame", "Back"))
        self.add_button.setText(_translate("Frame", "Add"))
        self.label.setText(_translate("Frame", "Rules"))
        self.rules.clicked.connect(self.changelabeltext)
        self.back.clicked.connect(self.back_to_main)
        self.add_words.clicked.connect(self.words)
        self.add_button.clicked.connect(self.insert_word)
        self.label.hide()
        self.label.setGeometry(QtCore.QRect(20, 70, 600, 450))
        # keeping the text of label empty before button get clicked
        self.label.setText("")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
