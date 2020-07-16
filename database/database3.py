import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="luminar",
    auth_plugin='mysql_native_password'

)

cursor = db.cursor()
sql="""insert into  Employee(
        FIRST_NAME ,
        LAST_NAME ,
        AGE ,
        SEX ) values ('AKHIL','M',28,'M')"""
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    db.rollback()
    print(e.args)

finally:
    db.close()

