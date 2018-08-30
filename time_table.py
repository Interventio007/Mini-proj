import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QPlainTextEdit, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
import datetime
import subprocess
import mysql.connector

class Window(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.rowcount()

    def initUI(self):

        self.mainWindow = QtWidgets.QWidget()
        self.mainWindow.setGeometry(0,0,1600,900)
        self.mainWindow.setWindowTitle("Time Table")

        self.row_size = int(self.row_entry.text())
        self.column_size = int(self.column_entry.text())

        self.tableWidget = QTableWidget(self.mainWindow)
        self.tableWidget.setRowCount(self.row_size)
        self.tableWidget.setColumnCount(self.column_size)
        
        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.verticalHeader().hide()

        self.resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.width = (self.resolution.width() / 2) - 500
        self.res_width = (self.frameSize().width() / 2) 

        print(self.width)
        print(self.res_width)

        self.tableWidget.move(self.width , (self.resolution.height() / 2) - (self.frameSize().height() / 2) ) 


        self.tableWidget.resize(1000,500)

        self.mainWindow.show()
    

    def rowcount(self):

        self.rowWindow = QtWidgets.QWidget()
        self.rowWindow.setGeometry(650,400,310,100)

        self.row_label = QtWidgets.QLabel(self.rowWindow)
        self.row_label.setText("Enter row size")
        
        self.row_entry = QtWidgets.QLineEdit(self.rowWindow)

        self.row_ok = QtWidgets.QPushButton("OK",self.rowWindow)

        self.row_ok.clicked.connect(self.row_ok_click)

        self.row_ok.move(220,70)
        self.row_label.move(25,35)
        self.row_entry.move(130,32)

        self.rowWindow.setFixedSize(310,100)

        self.rowWindow.show()

    
    def columncount(self):
        
        self.columnWindow = QtWidgets.QWidget()
        self.columnWindow.setGeometry(650,400,350,100)

        self.column_label = QtWidgets.QLabel(self.columnWindow)
        self.column_label.setText("Enter column size")
        
        self.column_entry = QtWidgets.QLineEdit(self.columnWindow)

        self.column_ok = QtWidgets.QPushButton("OK",self.columnWindow)

        self.column_ok.clicked.connect(self.column_ok_click)

        self.column_ok.move(250,70)
        self.column_label.move(25,35)
        self.column_entry.move(150,32)

        self.columnWindow.setFixedSize(350,100)

        self.columnWindow.show()

    def row_ok_click(self):

        self.columncount()
        self.rowWindow.close()

    def column_ok_click(self):

        self.initUI()
        self.columnWindow.close()


app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
