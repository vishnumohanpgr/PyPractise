"""
A program that helps you create a to-do list, with save feature.
"""
import os.path
import sys
import sqlite3
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication


# A global function that split a string in two & returns the second slice.
def clipper(txt):
    if "). " in txt:
        return txt.split("). ", 1)[1]
    else:
        return txt


# ==================== Main class.====================================
class ToDoList(QMainWindow):
    def __init__(self):
        super(ToDoList, self).__init__()
        uic.loadUi(uipath, self)
        self.loadup()  # Function that loads previously saved data from the database into the list.

        # ==================== Defining actions for events.====================================
        self.AddButton.clicked.connect(self.additem)
        self.EditButton.clicked.connect(self.edititem)
        self.RemoveButton.clicked.connect(self.removeitem)
        self.ClearButton.clicked.connect(self.clearlist)
        self.SaveButton.clicked.connect(self.savelist)
        self.UpButton.clicked.connect(self.moveup)
        self.DownButton.clicked.connect(self.movedown)
        self.ListHolder.itemClicked.connect(self.selectlistitem)

    # ==================== Defining all event-driven functions.====================================
    def additem(self):  # Function that adds new items into the list.
        if self.InputLine.text() != "":
            self.ListHolder.addItem(self.InputLine.text())  # Appends the item into the list from the input field.
            self.InputLine.setText("")  # Clears the input field after appending.
        self.refreshlist()

    def removeitem(self):  # Function that removes the selected item from the list.
        self.ListHolder.takeItem(self.ListHolder.currentRow())  # Removes the item at the current selected index.
        self.InputLine.setText("")  # Clears the input field after appending.
        self.refreshlist()

    def clearlist(self):  # Function that clears all items from the list.
        self.ListHolder.clear()

    def savelist(self):  # Saves the entire list into a database.
        curr.execute("DELETE FROM todo_list;",)  # Empties out the table inorder to avoid repetition.
        for i in range(self.ListHolder.count()):  # Going through every item in the list, one at a time.
            curr.execute("INSERT INTO todo_list(items) VALUES(?)", (clipper(self.ListHolder.item(i).text()), ))
            dbconnect.commit()  # Loads item at i into the database & commits the change.

        # Deliver a pop-up message box with notification of the save.
        savedmsg = QMessageBox()
        savedmsg.setWindowTitle("List saved to database!!")
        savedmsg.setText("The ToDo list has been successfully saved.")
        savedmsg.setIcon(QMessageBox.Information)
        savedmsg.exec()

    def loadup(self):   # The function that loads previously saved data from the database into the list widget.
        curr.execute("SELECT items FROM todo_list")
        temp = curr.fetchall()
        cnt = 1  # Serial number counter for each item in the list
        for i in temp:
            self.ListHolder.addItem(f'({cnt}). {str(i[0])}')
            cnt += 1  # Incrementing the counter

    def selectlistitem(self):  # Function that loads selected item into the input field.
        self.InputLine.setText(self.ListHolder.item(self.ListHolder.currentRow()).text())

    def moveup(self):  # Function that moves the selected item up the list.
        self.InputLine.setText("")  # Clears the input field after appending.
        if self.ListHolder.currentRow() != 0:  # Only run when selected item is not at the very top.
            self.ListHolder.insertItem(self.ListHolder.currentRow()-1,
                                       self.ListHolder.takeItem(self.ListHolder.currentRow()))
            self.refreshlist()

    def movedown(self):  # Moves the selected item down the list.
        self.InputLine.setText("")  # Clears the input field after appending.
        # Only run when selected item is not at the very bottom.
        if self.ListHolder.currentRow() != (self.ListHolder.count()-1):
            self.ListHolder.insertItem(self.ListHolder.currentRow()+1,
                                       self.ListHolder.takeItem(self.ListHolder.currentRow()))
            self.refreshlist()

    def edititem(self):  # Function that edits the selected item in the list.
        self.ListHolder.insertItem(self.ListHolder.currentRow(), self.InputLine.text())  # Insert item at index.
        self.ListHolder.takeItem(self.ListHolder.currentRow())  # Remove selected item.
        self.InputLine.setText("")  # Clear input field.

    def refreshlist(self):
        for i in range(self.ListHolder.count()):
            self.ListHolder.insertItem(i, f'({i+1}). {clipper(self.ListHolder.item(i).text())}')
            print(i,f'({i+1}). {clipper(self.ListHolder.item(i).text())}')
            self.ListHolder.takeItem(i+1)


# ==================== Executing main functions.====================================
BASEdir = os.path.dirname(os.path.abspath(__file__))  # Declaring the base directory as the current working directory.
dbpath = os.path.join(BASEdir, "ToDoList.db")  # Declaring absolute path to the database file.
uipath = os.path.join(BASEdir, "TodoList.ui")  # Declaring absolute path to the database file.
dbconnect = sqlite3.connect(dbpath)
curr = dbconnect.cursor()

# Creates a very simple table with only 1 column, called items.
curr.execute("CREATE TABLE IF NOT EXISTS todo_list(items TEXT)")

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
MainWindow = ToDoList()
widget.addWidget(MainWindow)
widget.setFixedSize(640, 720)
widget.setWindowTitle("ToDo")
widget.show()
app.exec()
dbconnect.commit()
dbconnect.close()
