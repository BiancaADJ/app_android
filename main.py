import sys
import time
import threading
from datetime import datetime
from tkinter import *
from sqlite3 import Cursor

# Imports de terceiros
import mysql.connector
from mysql.connector import Error
from PyQt6 import uic, QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import (
    QFileDialog, QApplication, QWidget, 
    QPushButton, QTableWidget, 
    QErrorMessage, QTimeEdit, QMainWindow
)
from PyQt5.QtCore import QTimer, QTime

app = QtWidgets.QApplication([])

# .ui
main = uic.loadUi('.ui/main.ui')
main.show()
app.exec()