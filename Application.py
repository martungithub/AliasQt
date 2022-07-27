from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(627, 573)
        self.play = QtWidgets.QPushButton(Frame)
        self.play.setGeometry(QtCore.QRect(210, 110, 231, 71))
        self.play.setObjectName("play")
        self.rules = QtWidgets.QPushButton(Frame)
        self.rules.setGeometry(QtCore.QRect(210, 230, 231, 71))
        self.rules.setObjectName("rules")
        self.add_words = QtWidgets.QPushButton(Frame)
        self.add_words.setGeometry(QtCore.QRect(210, 350, 231, 71))
        self.add_words.setObjectName("add_words")
        self.rules.raise_()
        self.play.raise_()
        self.add_words.raise_()

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.play.setText(_translate("Frame", "Play"))
        self.rules.setText(_translate("Frame", "Rules"))
        self.add_words.setText(_translate("Frame", "Add words"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
