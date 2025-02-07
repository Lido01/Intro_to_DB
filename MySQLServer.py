import mysql.connector
from mysql.connector import Error
# Database connection details (replace with your own)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234Lidetu",
    database="alx_be_book-store"
)
try:
     if db.is_connected():
         print("Database {database} created successfully!!")
     mycursor = mydb.cursor()
     mycursor.execute(""" CREATE DATABASE IF NOT EXISTS alx_book_store """)
     cursor.commit()
     cursor.close()
except mysql.connector.connect.Error as e:
    print("The error connecting to  my sql: {e}")
