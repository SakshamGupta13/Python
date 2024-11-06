import mysql
import mysql.connector

# create databased connection
connection = mysql.connector.connect(host = "localhost",username="root",password="saksham@2005",database="todo")

# to check the connection is established or not
if connection.is_connected():
    print("Database is Connected")
else:
    print("Database is not Connected")

    
#create a todo app task
createQuery = "create table if not exists task (taskname text, mobile text)"

# create cursor for mysql querry
mycursor = connection.cursor()

#to execute, create task table in database todo
mycursor.execute(createQuery)

# to comment or save the mysql querry
connection.commit()

# to insert task in todo database
inserttask="insert into task values('{}','{}')".format(input("Enter task name : "),input("Enter mobile number : "))
# inserttask="insert into task values('{}')".format(input("Enter mobile number : "))

# to execute the insert query
mycursor.execute(inserttask)

# to save the operation
connection.commit()

# update the task in database
updateTask = "update task set taskname = 'its vam' where mobile = '1111'"
mycursor.execute(updateTask)
connection.commit()

# to delete the task from database table
deleteTask = "delete from task where mobile ='22'"
mycursor.execute(deleteTask)
connection.commit()

# to access the data from database
myTask = "select * from task"
mycursor.execute(myTask)
print(mycursor.fetchall())
connection.commit()

# to drop the table
dropTask = "drop table task"
mycursor.execute(dropTask)
connection.commit()

# railway booking system
# flight booking system
# hotel mgmt
# library mgmt
# event mgmt