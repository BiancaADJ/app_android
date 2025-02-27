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
from PyQt6.QtWidgets import(
    QFileDialog, QApplication, QWidget, 
    QPushButton, QTableWidget, 
    QErrorMessage, QTimeEdit, QMainWindow
)
from PyQt6.QtCore import QTimer, QTime
from PyQt6.QtGui import QMovie
from gif_loader import add_gif_to_label

app = QtWidgets.QApplication([])

def new_note():
    post.show()

def main_close():
    main.close()
    note.show()

def inicio():
    main.show() # Pausar por 20 segundos antes de mudar de janela
    QTimer.singleShot(5000, main_close)

# .ui
main = uic.loadUi('.ui/main.ui')
note = uic.loadUi('.ui/note.ui')
post = uic.loadUi('.ui/post.ui')

# .gif_loader
label = main.findChild(QtWidgets.QLabel, "Qmove")
add_gif_to_label(label, "./assets/img/icons8-spinner.gif")

# botoes
add_note = note.add_note.clicked.connect(new_note)

inicio()
app.exec()