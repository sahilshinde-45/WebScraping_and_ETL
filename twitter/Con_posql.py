import psycopg2

class poconn():
    def __init__(self,host,database,user,password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = psycopg2.connect(host='localhost',user='postgres',password='',database=self.database)
    
    def createCursor(self):
        self.cur = self.conn.cursor()
        return self.cur

    def createTable(self,querry):
        return self.cur.execute(querry)
    
    def fetchData(self):
        self.cur.execute("select * from {}".format(self.table_name))
        return self.cur.fetchall()
    
    def fetchtable(self,table_name):
        self.table_name = table_name
        return table_name 

    def pushTable(self,pT):
        print(pT)
        for row in pT:
            print(row)        
            self.cur.execute("insert into {} values {}".format(self.table_name,tuple(row)))
            
    
    def retrive(self):
        self.cur.execute("select * from {}".format(self.table_name))

    def endConn(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

  
