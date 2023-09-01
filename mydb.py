import mysql.connector

database = mysql.connector.connect(
    user='root',
    password= 'Shashu@247',
    host = 'localhost',
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE elderco")
print("database created")