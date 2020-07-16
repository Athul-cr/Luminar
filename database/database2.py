import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="luminar",
    auth_plugin='mysql_native_password'

)

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS Employee")
sql="""CREATE TABLE Employee(
        FIRST_NAME CHAR(20),
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1))"""
try:
    cursor.execute(sql)
except Exception as e:
    print(e.args)

db.close()

