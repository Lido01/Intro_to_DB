# Datacase connection with python and error handling
import mysql.connector
from mysql.connector import Error
<<<<<<< HEAD
# Database connection details
=======
# Database connection details (replace with your own)
>>>>>>> 9661161149cbf2d58dc5112dc721fb3d89fd957e
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
<<<<<<< HEAD
except mysql.connector.connect.Error as e:
    print("The error connecting to  my sql: {e}")
=======
except mysql.connector.Error as err:
    print("The error to connect with sql: {err}")
>>>>>>> 9661161149cbf2d58dc5112dc721fb3d89fd957e
