"""
A program that reads user's first & last name in multiple dialog boxes, then displays the fullname in another.
"""
import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class FirstBox(QDialog):
    def __init__(self):
        super(FirstBox, self).__init__()  # Setting the super class for FirstBox as itself.

        loadUi("BoxFirst.ui", self)  # Loading the UI file

        # Describing event responses
        self.ButtonFirstSubmit.clicked.connect(self.firstnamesubmit)
        self.ButtonFirstReset.clicked.connect(self.firstnamereset)

    def firstnamesubmit(self):  # Function to be executed on clicking the submit button.
        curr.execute('INSERT INTO name_box(id, first_name) VALUES(?, ?)', (idgen(), self.LineEditFirst.text()))
        dbconnect.commit()
        self.LineEditFirst.setText("")  # Clearing the inout text field.

        # Jumping to another dialog box on button click
        lastbox = LastBox()  # Creating an instance of the dialog box to which we are switching.
        widget.addWidget(lastbox)  # Adding the newly created instance to the widget stack.
        widget.setCurrentIndex(1)  # Changing the current viewing widget to mentioned index.

    # Function that performs the label reset when the reset button is clicked.
    def firstnamereset(self):
        self.LineEditFirst.setText("")


class LastBox(QDialog):
    def __init__(self):
        super(LastBox, self).__init__()

        # Load the UI file
        loadUi("BoxLast.ui", self)

        # Describing event responses
        self.ButtonLastSubmit.clicked.connect(self.lastnamesubmit)
        self.ButtonLastReset.clicked.connect(self.lastnamereset)

    def lastnamesubmit(self):
        curr.execute('UPDATE name_box SET last_name=? WHERE id=? ', (self.LineEditLast.text(), idgen()-1))
        dbconnect.commit()
        self.LineEditLast.setText("")
        displaybox = DisplayBox()
        widget.addWidget(displaybox)
        widget.setCurrentIndex(2)

    # Function that performs the label reset when the reset button is clicked.
    def lastnamereset(self):
        self.LineEditLast.setText("")
        widget.setCurrentIndex(0)


class DisplayBox(QDialog):
    def __init__(self):
        super(DisplayBox, self).__init__()
        loadUi("BoxDisplay.ui", self)
        self.ButtonDisplayReset.clicked.connect(self.displayreset)
        curr.execute('SELECT first_name, last_name FROM name_box WHERE id=?', (idgen() - 1, ))
        temp = curr.fetchall()
        self.LabelDisplay.setText(f"{temp[0][0]} {temp[0][1]}")

    # Function that returns to the beginning on clicking the reset button
    def displayreset(self):
        widget.setCurrentIndex(0)


# Function that generates a unique id for each entry when required.
def idgen():
    i = 1
    curr.execute('SELECT id FROM name_box')
    temp = curr.fetchall()
    while i in [j[0] for j in temp]:
        i += 1
    return i


#  Database initialization.
dbconnect = sqlite3.connect('BoxDB.db')  # Connect to the database or if it doesn't exist, create a new one.
curr = dbconnect.cursor()  # creating a cursor for the specified database connection.

# Creating the table if it does not exist & describing its columns along with their data type.
curr.execute("""CREATE TABLE IF NOT EXISTS name_box(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT)
    """)

app = QApplication(sys.argv)  # Initializing the application into app
widget = QtWidgets.QStackedWidget()  # Creating a stack of widgets that we can switch between.
MainWindow = FirstBox()  # Creating an instance of FirstBox.
widget.addWidget(MainWindow)  # Adding the instance into the widget stack.
widget.setFixedSize(480, 360)  # Setting a fixed size for all the widgets.
widget.show()  # Displaying the widget stack.
app.exec()  # Running the PyQT5 application in the background.
dbconnect.commit()  # Committing all changes to the database
dbconnect.close()  # Closing the database connection.
