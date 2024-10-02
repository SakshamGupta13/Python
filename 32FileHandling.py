# create file for saving my laptop password
# open function will create the file when file is not exist and when file is not exist  and write the file
myPassword = open("password.txt","w")

# write my laptop password in file
myPassword.write("my password - saksham")

# overwrite the new password user input
# userPassword = input("Give Password : ")
# myPassword.write(userPassword)

# read the password from file
myPassword = open("password.txt","r")
print(myPassword.read())
myData = myPassword.read()
if "my" in myData:
    print("yes")
else:
    print("no")
    
# to close the file
myPassword.close()
# delete the file
import os
os.remove("password.txt")

# create read write csv, excel, json, txt
# create csv file
myCsv = open("myfile.csv","w")
myCsv.write("saksham,gupta,daksh")