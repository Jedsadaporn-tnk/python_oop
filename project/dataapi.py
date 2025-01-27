import database
mycursor = database.mydb.cursor()
import fastapi
app = fastapi.FastAPI()

@app.get('/show/{table}')    
async def selecctdb(table):
            sql = f'select * from {table}'
            mycursor.execute(sql)
            show = mycursor.fetchall()
            return show

@app.get('/insertus/{name},{password}/{email}/{role}')
async def insertus(name,password,email,role):
    sql = 'insert into user values (%s, %s, %s, %s, %s)'
    val_sql = (None,name,password,email,role)
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0 :
        return True
    else:
        return False
    
@app.get('/isnertor/{usid}/{date}/{amount}/{sta}/{prid}')
async def insertor(usid,date,amount,sta,prid):
    sql = 'insert into order values (%s, %s, %s, %s, %s)'
    val_sql = (None,usid,date,amount,sta,prid)
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0 :
        return True
    else:
        return False

@app.get('/insertca/{name}')
async def insertca(name):
    sql = 'insert into categories values (%s, %s, %s, %s, %s)'
    val_sql = (None,name)
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0 :
        return True
    else:
        return False
@app.get('/insertpd/{name}/{des}/{price}/{stock}/{id}')
async def insertca(name,des,price,stock,id):
    sql = 'insert into product values (%s, %s, %s, %s, %s)'
    val_sql = (None,name,des,price,stock,id)
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0 :
        return True
    else:
        return False
    
@app.get('/delete/{table}/{id}')
async def dele(table,id):
    sql = f'Delete from {table} where user_id = {id}'
    mycursor.execute(sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
    

@app.get('/edit/{table}/{colum}/{idname}/{val}/{id}')
def editdb(table,colum,idname,val,id):
    sql = f'UPDATE {table} SET {colum} = " %s" WHERE {idname} = %s'
    val_sql = (val,id)
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False

