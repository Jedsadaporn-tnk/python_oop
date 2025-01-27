import mysql.connector
import fastapi 
app = fastapi.FastAPI()

class managedb:
    def __init__(self,host,user,password,database):
            self.mydb = mysql.connector.connect (
                host = host,
                user = user,
                password = password,
                database = database
                )
            self.mycursor = self.mydb.cursor()
            
    @app.get('/show/{table}')       
    async def selecctdb (self,table):
            sql = f'select * from {table}'
            self.mycursor.execute(sql)
            show = self.mycursor.fetchall()
            return show
    def insertus(self,name,password,email,role):
            sql = 'insert into user values (%s ,%s ,%s ,%s ,%s)'
            val_sql = (None,name,password,email,role)
            self.mycursor.execute(sql,val_sql)
            self.mydb.commit()
            if self.mycursor.rowcount > 0 :
                return True
            else:
                return False
    def insertor(self,usid,date,amount,sta,prid):
            sql = 'insert into order  values (%s ,%s ,%s ,%s ,%s ,%s)'
            val_sql = (None,usid,date,amount,sta,prid)
            self.mycursor.execute(sql,val_sql)
            self.mydb.commit()
            if self.mycursor.rowcount > 0 :
                return True
            else:
                return False
    def insertca(self,name):
            sql = 'insert into categories  values (%s ,%s)'
            val_sql = (None,name)
            self.mycursor.execute(sql,val_sql)
            self.mydb.commit()
            if self.mycursor.rowcount > 0 :
                return True
            else:
                return False
    def insertva(self,name,des,price,stock,id):
            sql = 'insert into product values (%s ,%s ,%s ,%s ,%s ,%s)'
            val_sql = (None,name,des,price,stock,id)
            self.mycursor.execute(sql,val_sql)
            self.mydb.commit()
            if self.mycursor.rowcount > 0 :
                return True
            else:
                return False
    def delete(self,table,id):
        sql = f'delete from {table} where user_id = {id}'
        self.mycursor.execute(sql)
        show = self.mycursor.fetchall()
        return show
    def editdb(self,table,colum,idname,val,id):
        sql = f'UPDATE {table} SET {colum} = " %s" WHERE {idname} = %s'
        val_sql = (val,id)
        self.mycursor.execute(sql,val_sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False
