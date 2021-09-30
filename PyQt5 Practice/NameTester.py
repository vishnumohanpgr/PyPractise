"""
A simple program that creates a GUI which prints out your name.
"""
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QTextEdit


class NameTest(QDialog):
    def __init__(self):
        super().__init__()

        # Loading the ui file from designer
        uic.loadUi("NameTester.ui", self)

        # Addressing the widgets [Optional]
        self.Mlabel = self.findChild(QLabel, "Label")
        self.Mtextedit = self.findChild(QTextEdit, "TextEdit")
        self.Msubmitbutton = self.findChild(QPushButton, "SubmitButton")
        self.Mresetbutton = self.findChild(QPushButton, "ResetButton")

        # Describing a event responses
        self.Msubmitbutton.clicked.connect(self.clicksubmit)
        self.Mresetbutton.clicked.connect(self.clickreset)

        # Display the app
        self.show()

    # Function that performs the label change action when the submit button is clicked.
    def clicksubmit(self):
        self.Mlabel.setText(f'Hello there, {self.Mtextedit.toPlainText()}')
        self.Mtextedit.setPlainText("")

    # Function that performs the label reset when the reset button is clicked.
    def clickreset(self):
        self.Mlabel.setText('Enter your name')
        self.Mtextedit.setPlainText("")


# Initializing the app
app = QApplication(sys.argv)
MainWindow = NameTest()
app.exec()
