import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QPlainTextEdit, QDesktopWidget
from PyQt5.QtGui import QIconimport sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QPlainTextEdit, QDesktopWidget, QComboBox
from PyQt5.QtGui import QIcon 
from PyQt5.QtCore import pyqtSlot
import datetime
import subprocess
import mysql.connector
import csv
import itertools

global count
count = 0

class Window(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.database_create()
        
        self.mycursor.execute("USE Time_Table") 
        self.mycursor.execute("SHOW TABLES")
        tables = self.mycursor.fetchone() 
        
        if tables == None:
            self.rowcount()

        else:
            self.initUI()
            self.csv_read()
       
        

    def initUI(self): 

        self.mainWindow = QtWidgets.QWidget()
        self.mainWindow.setGeometry(0,0,1600,900)
        self.mainWindow.setWindowTitle("Time Table")

        self.mycursor.execute("USE Time_Table") 
        self.mycursor.execute("Select * from csv_check")
        tables = self.mycursor.fetchone() 

        self.row_size = int(tables[0])
        self.column_size = int(tables[1])

        self.tableWidget = QTableWidget(self.mainWindow)
        self.tableWidget.setRowCount(self.row_size)
        self.tableWidget.setColumnCount(self.column_size)

        self.drp_box_lbl = QtWidgets.QLabel(self.mainWindow)
        self.drp_box_lbl.setText("Semester:")
        self.drop_box = QComboBox(self.mainWindow)

        self.drop_box.addItem("Semester 1")
        self.drop_box.addItem("Semester 2")
        self.drop_box.addItem("Semester 3")
        self.drop_box.addItem("Semester 4")
        self.drop_box.addItem("Semester 5")
        self.drop_box.addItem("Semester 6")
        self.drop_box.addItem("Semester 7")
        self.drop_box.addItem("Semester 8")

        self.save_button = QtWidgets.QPushButton("Save",self.mainWindow)
        
        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.verticalHeader().hide()

        self.resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.width = (self.resolution.width() / 2) - 650
        self.height = (self.resolution.height() / 2) - 250

        self.frame_size = self.mainWindow.frameGeometry()

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

        self.drp_box_lbl.move((self.frame_size.width() - 1525),(self.frame_size.height() - 760))
        self.drop_box.move((self.frame_size.width() - 1450),(self.frame_size.height() - 800))
        self.drop_box.resize(200,100)
        
        
        self.save_button.move((self.frame_size.width() - 300),(self.frame_size.height() - 175))
        self.save_button.resize(75,50)
        self.save_button.clicked.connect(self.csv_write)

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
            if a[0] == 'csv_check':
                self.table_exists = True
        
        if self.table_exists == False:
          self.mycursor.execute("create table csv_check(row_value int,col_val int,val_Check tinyint(1))")

    def table_insert(self):

        row_size = int(self.row_entry.text())
        col_size = int(self.column_entry.text())

        sql = "INSERT INTO csv_check (row_value,col_val,val_check) VALUE (%s,%s,%s)"
        val =[row_size,col_size,self.csv_check]
        self.mycursor.execute(sql, val)

        self.mydb.commit()

        

    def csv_write(self):
        
        with open("/Users/srinivas/output_csv","w") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            for i in range(0,self.row_size):
                for j in range(0,self.column_size):
                    item = self.tableWidget.item(i,j)
                    if(item == None):
                        writer.writerow(["NULL"])
                    else:
                        writer.writerow([item.text()])

                   
    def csv_read(self):

    
        with open('/Users/srinivas/output_csv', newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            value =[]
            for val in reader:
                value.append(val)
            for i in range(0,self.row_size):
                for j in range(0,self.column_size): 
                      
                    global count
                    if (value[count] == "NULL"):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(""))
                      
                    else:
                        gg = next(iter(value[count]))
                        self.tableWidget.setItem(i, j, QTableWidgetItem(gg))

                    count+=1
        

            

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

        self.database_table()
    

    def row_ok_click(self):

        self.columncount()
        self.rowWindow.close()

    def column_ok_click(self):

        self.csv_check = True
        self.table_insert()

        self.initUI()
        self.columnWindow.close()
       


app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
from PyQt5.QtCore import pyqtSlot, Qt
import datetime
import subprocess
import mysql.connector
import csv
import itertools

global count
count = 0

class Window(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.database_create()
        
        self.mycursor.execute("USE Time_Table") 
        self.mycursor.execute("SHOW TABLES")
        tables = self.mycursor.fetchone() 
        
        if tables == None:
            self.rowcount()

        else:
            self.initUI()
            self.csv_read()
       
        

    def initUI(self): 

        self.mainWindow = QtWidgets.QWidget()
        self.mainWindow.setGeometry(0,0,1600,900)
        self.mainWindow.setWindowTitle("Time Table")

        self.mycursor.execute("USE Time_Table") 
        self.mycursor.execute("Select * from csv_check")
        tables = self.mycursor.fetchone() 

        self.row_size = int(tables[0])
        self.column_size = int(tables[1])

        self.tableWidget = QTableWidget(self.mainWindow)
        self.tableWidget.setRowCount(self.row_size)
        self.tableWidget.setColumnCount(self.column_size)

        self.save_button = QtWidgets.QPushButton("Save",self.mainWindow)
        
        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.verticalHeader().hide()

        self.resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.width = (self.resolution.width() / 2) - 650
        self.height = (self.resolution.height() / 2) - 250

        self.frame_size = self.mainWindow.frameGeometry()

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

        self.save_button.move((self.frame_size.width() - 500),(self.frame_size.height() - 250))
        self.save_button.resize(75,50)
        self.save_button.clicked.connect(self.csv_write)

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
            if a[0] == 'csv_check':
                self.table_exists = True
        
        if self.table_exists == False:
          self.mycursor.execute("create table csv_check(row_value int,col_val int,val_Check tinyint(1))")

    def table_insert(self):

        row_size = int(self.row_entry.text())
        col_size = int(self.column_entry.text())

        sql = "INSERT INTO csv_check (row_value,col_val,val_check) VALUE (%s,%s,%s)"
        val =[row_size,col_size,self.csv_check]
        self.mycursor.execute(sql, val)

        self.mydb.commit()

        

    def csv_write(self):
        
        with open("/Users/srinivas/output_csv","w") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            for i in range(0,self.row_size):
                for j in range(0,self.column_size):
                    item = self.tableWidget.item(i,j)
                    if(item == None):
                        writer.writerow(["NULL"])
                    else:
                        writer.writerow([item.text()])

                   
    def csv_read(self):

    
        with open('/Users/srinivas/output_csv', newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            value =[]
            for val in reader:
                value.append(val)
            for i in range(0,self.row_size):
                for j in range(0,self.column_size): 
                      
                    global count
                    if (value[count] == "NULL"):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(""))
                      
                    else:
                        gg = next(iter(value[count]))
                        self.tableWidget.setItem(i, j, QTableWidgetItem(gg))

                    count+=1
        

            

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

        self.database_table()
    

    def row_ok_click(self):

        self.columncount()
        self.rowWindow.close()

    def column_ok_click(self):

        self.csv_check = True
        self.table_insert()

        self.initUI()
        self.columnWindow.close()
       


app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
