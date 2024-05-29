import mysql.connector
from mysql.connector.constants import CharacterSet
import fileClass
import csv

class Mysql():

    def __init__(self,host,database,user,password):
        self.host = host
        self.database=database
        self.user = user
        self.password = password
        self.mydb = mysql.connector.connect(host='localhost',user='root',password='',database=self.database,use_unicode=True)
    
    def createCursor(self):
        self.cursor = self.mydb.cursor()
        return self.cursor
    
    def fetchData(self):
        self.cursor.execute("select * from {}".format(self.table_name))
        return self.cursor.fetchall()
    
    def createTable(self,cT):
        return self.cursor.execute(cT)
        

    def fetchtable(self,table_name):
        self.table_name = table_name
        
        return self.table_name 

    def pushTable(self,pT):

        for row in pT:
            
            self.cursor.execute("insert into {} values {}".format(self.table_name,tuple(row)))
   
    def retrive(self):
        self.cursor.execute("select * from {}".format(self.table_name))

    def endConn(self):
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()
