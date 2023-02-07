import mysql.connector
class Mysql_DBaccess:
    def __init__(self,host,db,user,password):
        self.host=host
        self.user=user
        self.password=password
        self.db=db
        try:
            self.connection=mysql.connector.connect(host=self.host,database=self.db,user=self.user,password=self.password)
        except Exception as e:
            print(e)
            print("Error while connecting to the database")
    def insert_data(self,filename):
        self.filename=filename
        self.cur = self.connection.cursor()
        sql="insert into files(filename)values(%s);"
        val=(self.filename)
        self.cur.execute(sql,(val,))
        self.connection.commit()

    def searchDB(self,fil):
        self.f="filename"
        sql="select*from files where filename like '%{0}'".format(fil)
        self.cur.execute(sql)
        row=self.cur.fetchone()
        if row==None:
            return 0
        else:
            print(row)
dbobj=Mysql_DBaccess('localhost','searchfiles','root','root@123')
dbobj.insert_data("c://hcl//demo.txt")
dbobj.searchDB("c://"
               ""
               "hcl//demo.txt")



