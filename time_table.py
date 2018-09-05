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
        self.database_create()
        self.database_table()

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
        self.width = (self.resolution.width() / 2) - 650
        self.height = (self.resolution.height() / 2) - 250

        self.tableWidget.move(self.width,self.height ) 

        self.tableWidget.setColumnWidth(0,125)
        self.tableWidget.setColumnWidth(1,125)
        self.tableWidget.setColumnWidth(2,125)
        self.tableWidget.setColumnWidth(3,150)
        self.tableWidget.setColumnWidth(4,125)
        self.tableWidget.setColumnWidth(5,125)
        self.tableWidget.setColumnWidth(6,150)
        self.tableWidget.setColumnWidth(7,125)
        self.tableWidget.setColumnWidth(8,125)
        self.tableWidget.setColumnWidth(9,125)
        
        self.tableWidget.setRowHeight(0,50)
        self.tableWidget.setRowHeight(1,50)
        self.tableWidget.setRowHeight(2,50)
        self.tableWidget.setRowHeight(3,50)
        self.tableWidget.setRowHeight(4,50)
        self.tableWidget.setRowHeight(5,50)
        self.tableWidget.setRowHeight(6,50)
        self.tableWidget.setRowHeight(7,50)
        self.tableWidget.setRowHeight(8,50)
        self.tableWidget.setRowHeight(9,50)
        
        self.tableWidget.resize(1302,502)

        self.mainWindow.show()


    def database_create(self):

        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        buffered = True
        )

        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("SHOW DATABASES")
        self.db_exists = False
        
        for x in self.mycursor:

            if x[0] == 'Time_Table':
                self.db_exists = True
        
        if self.db_exists == False:
            self.mycursor.execute("CREATE DATABASE Time_Table")
            

    def database_table(self):
        
        self.mycursor.execute("use Time_Table")
        self.mycursor.execute("show tables")
        self.table_exists = False

        for a in self.mycursor:
            if a[0] == 'Time_Day':
                self.table_exists = True
        
        if self.table_exists == False:
            self.mycursor.execute("Create Table Time_Day(Time Varchar(10), Day Varchar(10))")
    

    def rowcount(self):

        self.rowWindow = QtWidgets.QWidget()
        
        self.resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.window_1_width = (self.resolution.width() / 2) - 150
        self.window_1_height = (self.resolution.height() / 2) - 50

        self.rowWindow.setGeometry(self.window_1_width,self.window_1_height,310,100)

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
        
        self.resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.window_2_width = (self.resolution.width() / 2) - 175
        self.window_2_height = (self.resolution.height() / 2) - 50
        
        self.columnWindow.setGeometry(self.window_2_width,self.window_2_height,350,100)

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
