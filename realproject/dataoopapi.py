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


      
    def selecctdb (self,table):
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
    def insertbg(self,length,Width,Thickness):
                sql = 'insert into barget values (%s ,%s ,%s ,%s )'
                val_sql = (None,length,Width,Thickness)
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
            
db = {
        'market' : managedb(host='localhost',user='root',password='o8iLiuTii,ik=',database='market'),
        'barget' : managedb(host='localhost',user='root',password='o8iLiuTii,ik=',database='barget')
}

@app.get('/show/{database}/{table}')       
async def selecctdb (database,table):
                all_db = db[database]
                result = all_db.selecctdb(table)
                return {'selecctdb' : result}
@app.get('/insertus/{database}/{name}/{password}/{email}/{role}')
async def insertus(database,name,password,email,role):
                all_db = db[database] 
                result =all_db.insertus(name,password,email,role)
                return {'insertuser ': result}
@app.get('/isnertor/{database}/{date}/{amount}/{sta}/{prid}')
def insertor(database,date,amount,sta,prid):
                all_db = db[database] 
                result =all_db.insertus(date,amount,sta,prid)
                return {'insertorder ': result}
@app.get('/insertca/{name}')
def insertca(database,name):
                all_db = db[database] 
                result =all_db.insertus(name)
                return {'insertcategories ': result}
@app.get('/insertproduct/{database}/{name}/{des}/{price}/{stock}/{id}')
def insertva(database,name,des,price,stock,id):
                all_db = db[database] 
                result =all_db.insertus(name,des,price,stock,id)
                return {'insertproduct ': result}
@app.get('/insertbarget/{database}/{length}/{Width}/{Thickness}')
def insertbg(database,length,Width,Thickness):
                all_db = db[database] 
                result =all_db.insertbg(length,Width,Thickness)
                return {'insertnarget ': result}
@app.get('/delete/{table}/{id}')
def delete(database,table,id):
            all_db = db[database] 
            result =all_db.insertus(table,id)
            return {'delete ': result}
@app.get('/edit/{table}/{colum}/{idname}/{val}/{id}')
def editdb(database,table,colum,idname,val,id):
            all_db = db[database] 
            result =all_db.insertus(table,colum,idname,val,id)
            return {'edit ': result}