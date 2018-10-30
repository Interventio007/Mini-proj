import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QPlainTextEdit, QDesktopWidget, QComboBox
from PyQt5.QtGui import QIcon 
from PyQt5.QtCore import pyqtSlot
# from PyQt5.QtCore import *
from PyQt5 import QtCore
import datetime
import subprocess
import mysql.connector
import csv
import itertools
import os

class Window(QtWidgets.QWidget):
     
    def __init__(self):
        super().__init__()
        self.init_ui()

    
    def init_ui(self):

        self.detail_Window = QtWidgets.QWidget()
        self.resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.window_width = (self.resolution.width() / 2) - 300
        # self.window_height = (self.resolution.height() / 2)
        self.detail_Window.setGeometry(self.window_width,0,600,700)
        self.detail_Window.setWindowTitle("Time Table")

        vbox_1 = QtWidgets.QVBoxLayout(self.detail_Window)
        self.name_lbl = QtWidgets.QLabel()
        self.name_lbl.setText("Please Fill in the required details for the time table")
        vbox_1.addWidget(self.name_lbl)
        vbox_1.setGeometry(QtCore.QRect(10,10,550,50))
        
      

        vbox_2 = QtWidgets.QVBoxLayout(self.detail_Window)
        self.name_lbl_1 = QtWidgets.QLabel()
        self.name_lbl_1.setText("Please Fill in the required details for the time table")
        vbox_2.addWidget(self.name_lbl)
        vbox_2.setGeometry(QtCore.QRect(10,10,550,50))

       

        vbox_3 = QtWidgets.QVBoxLayout(self.detail_Window)
        self.name_lbl_2 = QtWidgets.QLabel()
        self.name_lbl_2.setText("Please Fill in the required details for the time table")
        vbox_3.addWidget(self.name_lbl)
        vbox_3.setGeometry(QtCore.QRect(10,10,550,50))
        
        
        
        self.detail_Window.show()



app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
