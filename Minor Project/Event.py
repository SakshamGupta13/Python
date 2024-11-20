import mysql
import mysql.connector

#create database connection
connection = mysql.connector.connect(host = "localhost" , username = "root" , password = "saksham@2005" , database = "event")

# to check the connection is establish or not
if connection.is_connected():
    print("Database is connected")
else:
    print("Database is not connected")

# Press 1 to add new event : eventname , eventdate , venue , eventid
# Press 2 to get all event
# Press 3 to delete event 
# Press 4 to update event 
# Press 5 to add student in event : studentname , stuemail , stumobile , studept , stuyear  , eventname
# Press 6 to get all student
# Press 7 to delete student
# Press 8 to update student

eventdata = "create table if not exists eventdata(eventname text , eventdate text , venue text , eventid text)"
mycursor = connection.cursor()
mycursor.execute(eventdata)
connection.commit()
print("Press 1 to Add New Event : ")
print("Press 2 to get all Event : ")
print("Press 3 to delete Event : ")
print("Press 4 to update Event : ")
print("Press 5 to add Student in Event : ")
print("Press 6 to get all Student : ")
print("Press 7 to delete Student : ")
print("Press 8 to update Student : ")

select = int(input("enter no. 1 to 8 : "))
# to add the new event
if(select==1):
    insertevent ="insert into eventdata values('{}' , '{}' , '{}' , '{}')".format(input("Enter Event name : ") , input("Enter Event date : ") , input("Enter Venue : ") , int(input("enter eventid ")))
    mycursor.execute(insertevent)
    connection.commit()

# to get all events
elif(select==2):
    myevent = "select * from eventdata"
    mycursor.execute(myevent)
    print(mycursor.fetchall())
    connection.commit()
    
# to delete the event
elif(select==3):
    deletevent = "delete from eventdata where eventid ='1'"
    mycursor.execute(deletevent)
    connection.commit()

# to update the event
elif(select==4):
    updatevent = "update eventdata set eventname = 'NIGHT PARTY' , eventdate = '19.11.24' , venue = 'CHANAKYA AUDITORIUM' where eventid = '1'"
    mycursor.execute(updatevent)
    connection.commit()
        
studentdata = "create table if not exists studentdata(studname text , studemail text , studmobile text , studept text , studyear text , eventname text , studentid text)"
mycursor.execute(studentdata)
connection.commit()

# to add the student data
if(select==5):
    insertstudata = "insert into studentdata values('{}' , '{}' , '{}' , '{}' , '{}' , '{}' , '{}')".format(input("Enter Student Name : ") , input("Enter Student email : ") , int(input("Enter Student Mobile Number : ")) , input("Enter Student Department Name : ") , int(input("Enter Graduation Year : ")) , input("Enter Event Name : ") , int(input("Enter Student Id : ")))
    mycursor.execute(insertstudata)
    connection.commit()    

# to get all student
elif(select==6):
    mystudata = "select * from studentdata"
    mycursor.execute(mystudata)
    print(mycursor.fetchall())
    connection.commit()

# to delete the student
elif(select==7):
    deletestudata = "delete from studentdata where studentid = '1'"
    mycursor.execute(deletestudata)
    connection.commit()

# to update the student data
elif(select==8):
    updatestudata  = "update studentdata set studyear = '3' where studentid = '1'"
    mycursor.execute(updatestudata)
    connection.commit()
    
else:
    print("you have selected out of the range no.")