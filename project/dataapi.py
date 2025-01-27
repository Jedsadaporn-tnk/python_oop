import database
mycursor = database.mydb.cursor()
import fastapi
app = fastapi.FastAPI()

@app.get('/show/')
async def selecctdb ():
            sql = f'select * from user'
            mycursor.execute(sql)
            show = mycursor.fetchall()
            return show

@app.get('/insert/')
async def insert():
    sql = 'insert into user values (%s, %s, %s, %s, %s)'
    val_sql = (1,'Itui',1234,'Itui@gmail.com','customer')
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0 :
        return True
    else:
        return False
    
@app.get('/delete/')
async def dele():
    sql = f'Delete from user where user_id = 1'
    mycursor.execute(sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
    

@app.get('/edit/')
async def editdb():
    sql = f'UPDATE user SET username = "IlookAof" WHERE user_id = 1'

    mycursor.execute(sql,)
    database.mydb.commit()

    if mycursor.rowcount > 0:
        return True
    else:
        return False
