import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="luminar",
    auth_plugin='mysql_native_password'

)

cursor = db.cursor()
sql="""select FIRST_NAME from Employee where age<28
        """
try:
    cursor.execute(sql)
    data=cursor.fetchall()
    print(data)
except Exception as e:
    print(e.args)

db.close()

