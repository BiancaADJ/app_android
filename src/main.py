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
from PyQt6.QtCore import QTimer, QTime
from PyQt6.QtGui import QMovie
from gif_loader import add_gif_to_label

app = QtWidgets.QApplication([])

def main_close():
    main.close()

def inicio():
    main.show() # Pausar por 5 segundos antes de mudar de janela
    QTimer.singleShot(5000, main_close)
    note.show()

# .ui
main = uic.loadUi('.ui/main.ui')
note = uic.loadUI('.ui/note.ui')

# .gif_loader
label = main.findChild(QtWidgets.QLabel, "Qmove")
add_gif_to_label(label, "./img/icons8-spinner.gif")



inicio()
app.exec()