import mysql.connector
import MySQLdb


dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='TrongNguyen041096'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE CRM_app")

print("All Done")
