import mysql
import mysql.connector

# create databased connection
connection = mysql.connector.connect(host = "localhost",username="root",password="saksham@2005",database="its")

# to check the connection is established or not
if connection.is_connected():
    print("Database is Connected")
else:
    print("Database is not Connected")