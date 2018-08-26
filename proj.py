import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QPlainTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import datetime
import subprocess
import mysql.connector


class Window(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.database_create()
        self.mycursor.execute("use Bill")
        self.table_show = self.mycursor.execute("Show tables")
        self.table_check = self.mycursor.fetchone()
        
        if self.table_check == None:
            self.database_table()
            self.name()
        else:
            self.initUI()
           
        

    def name(self):

        self.windows = QtWidgets.QWidget()

        self.l_name = QtWidgets.QLabel(self.windows)
        self.l_name.setText("Name")
        
        self.e_name = QtWidgets.QLineEdit(self.windows)

        self.b_ok = QtWidgets.QPushButton("OK",self.windows)

        self.b_ok.move(220,70)
        self.l_name.move(50,35)
        self.e_name.move(100,35)

        self.windows.setGeometry(500,400,310,100)
        self.windows.show()

        self.initial_check = True
        self.b_ok.clicked.connect(self.ok_click)

    def phone(self):

        self.window_phone = QtWidgets.QWidget()

        self.l_phone_name = QtWidgets.QLabel(self.window_phone)
        self.l_phone_name.setText("Phone")
        
        self.e_phone_name = QtWidgets.QLineEdit(self.window_phone)

        self.b_ok_1 = QtWidgets.QPushButton("OK",self.window_phone)

        self.b_ok_1.move(220,70)
        self.l_phone_name.move(50,35)
        self.e_phone_name.move(100,35)

        self.window_phone.setGeometry(500,400,310,100)
        self.window_phone.show()

        self.b_ok_1.clicked.connect(self.ok_click_phone)
       

    def address(self):
        
        self.windows_1 = QtWidgets.QWidget()

        self.L1_name = QtWidgets.QLabel(self.windows_1)
        self.L1_name.setText("Address")
        
        self.E1_name = QtWidgets.QPlainTextEdit(self.windows_1)

        self.b_ok_2 = QtWidgets.QPushButton("OK",self.windows_1)

        self.b_ok_2.move(330,125)
        self.L1_name.move(50,40)
        self.E1_name.move(110,40)

        self.E1_name.resize(300,75)

        self.windows_1.setGeometry(500,400,500,200)
        self.windows_1.show()

        self.b_ok_2.clicked.connect(self.ok_click_address)

       
    def ok_click(self):

        self.phone()

        self.windows.close()

    def ok_click_phone(self):

        self.address()

        self.window_phone.close()

    def ok_click_address(self):

        self.database_values()

        self.initUI()

        
        self.windows_1.close()

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

            if x[0] == 'Bill':
                self.db_exists = True
        
        if self.db_exists == False:
            self.mycursor.execute("CREATE DATABASE Bill")

    def database_table(self):
        
        self.mycursor.execute("use Bill")
        self.mycursor.execute("show tables")
        self.table_exists = False

        for a in self.mycursor:
            if a[0] == 'billDetails':
                self.table_exists = True
        
        if self.table_exists == False:
            self.mycursor.execute("Create Table billDetails(Name varchar(20),phoneNo varchar(10),address varchar(120),initialcheck varchar(5))")

    def database_values(self):

        self.shop_name = self.e_name.text()
        self.shop_phone = int(self.e_phone_name.text())
        self.shop_address = self.E1_name.toPlainText()

        self.query = "insert into billDetails(Name,phoneNo,address,initialcheck) values(%s,%s,%s,%s)"
        self.values = (self.shop_name,self.shop_phone,self.shop_address,self.initial_check)

        self.mycursor.execute(self.query,self.values)
        self.mydb.commit()

    def database_retrieve(self):

        self.mycursor.execute("SELECT * FROM billDetails")
        self.shop_values_retreived = self.mycursor.fetchone()
        
    def initUI(self):
        
        self.database_retrieve()

        self.screen = app.primaryScreen()
        self.size = self.screen.size()
        self.screen_width = self.size.width()
        self.screen_height = self.size.height()

        self.w = QtWidgets.QWidget()
        self.w.setGeometry(0,0,1920,1080)
        self.w.setWindowTitle("GreenBill")

        self.l1_image = QtWidgets.QLabel(self.w)
        self.l1_title = QtWidgets.QLabel(self.w)

        self.l1_image.setPixmap(QtGui.QPixmap("/Users/srinivas/Downloads/gg.png"))
        self.l1_title.setText("Green Bill")

        self.setStyleSheet("QtLabel {font: 50pt Roboto}")
        self.l1_title.setStyleSheet("font: 50pt Roboto")
          
        self.l1_image.move(50,25)
        self.l1_title.move(125,25)

        self.l1_bill = QtWidgets.QLabel(self.w)
        self.l1_name = QtWidgets.QLabel(self.w)
        self.l1_phone = QtWidgets.QLabel(self.w)

        self.l1_bill.setStyleSheet("font: 20pt Roboto")
        self.l1_name.setStyleSheet("font: 20pt Roboto")
        self.l1_phone.setStyleSheet("font: 20pt Roboto")

        self.l1_bill.setText("Bill No")
        self.l1_name.setText("Name")
        self.l1_phone.setText("Phone")

        self.e1_bill = QtWidgets.QLineEdit(self.w)
        self.e1_name = QtWidgets.QLineEdit(self.w)
        self.e1_phone = QtWidgets.QLineEdit(self.w)

        self.e1_name.setText("{0}".format(self.shop_values_retreived[0]))
        self.e1_phone.setText("{0}".format(self.shop_values_retreived[1]))
        
        self.l1_bill.move(50,150)
        self.l1_name.move(50,200)
        self.l1_phone.move(50,250)

        if self.screen_width == 1600 and self.screen_height == 900:

            self.e1_bill.move(150,155)
            self.e1_name.move(150,205)
            self.e1_phone.move(150,255)

        else:

            self.e1_bill.move(125,150)
            self.e1_name.move(125,200)
            self.e1_phone.move(125,250)

        self.e1_bill.resize(200,25)
        self.e1_name.resize(200,25)
        self.e1_phone.resize(200,25)

        self.l2_date = QtWidgets.QLabel(self.w)
        self.l2_address = QtWidgets.QLabel(self.w)

        self.e2_date = QtWidgets.QLineEdit(self.w)
        self.e2_address = QtWidgets.QPlainTextEdit(self.w)

        self.e2_address.insertPlainText("{0}".format(self.shop_values_retreived[2]))

        self.l2_date.setText("Date")
        self.l2_address.setText("Address")

        self.l2_date.setStyleSheet("font: 20pt Roboto")
        self.l2_address.setStyleSheet("font: 20pt Roboto")

        self.l2_date.move(400,150)
        self.l2_address.move(400,200)
       
        if self.screen_width == 1600 and self.screen_height == 900:
            
            self.e2_date.move(525,155)
            self.e2_address.move(525,205)
       
        else:
            
            self.e2_date.move(500,150)
            self.e2_address.move(500,200)


        self.e2_date.resize(200,25)
        self.e2_address.resize(300,75)

        self.tableWidget = QTableWidget(self.w)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(12)
        
        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.verticalHeader().hide()
        
        self.tableWidget.setItem(0,0, QTableWidgetItem("Serial No"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Item Code"))
        self.tableWidget.setItem(0,3, QTableWidgetItem("Product Name"))
        self.tableWidget.setItem(0,6, QTableWidgetItem("Quantity"))
        self.tableWidget.setItem(0,7, QTableWidgetItem("Unit Price"))
        self.tableWidget.setItem(0,8, QTableWidgetItem("GST"))
        self.tableWidget.setItem(0,9, QTableWidgetItem("Total"))

        self.tableWidget.setSpan(0,1,1,2)
        self.tableWidget.setSpan(0,3,1,3)
        self.tableWidget.setSpan(0,9,1,2)
        
        
        self.tableWidget.move(50,300)
        self.tableWidget.resize(1325,400)

        self.b_save = QtWidgets.QPushButton("Save",self.w)
        self.b_print = QtWidgets.QPushButton("Print",self.w)


        self.b_save.move(1150,725)
        self.b_print.move(1275,725)

        self.b_save.resize(100,50)
        self.b_print.resize(100,50)


        self.time = datetime.datetime.now()
        self.day = self.time.day
        self.month = self.time.month
        self.year = self.time.year

        self.e2_date.setText("{0}/{1}/{2} ".format(self.day,self.month,self.year))

        self.w.show()

    
    
    
app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_()) 
