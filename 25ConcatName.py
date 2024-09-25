# create function to contenate fname and lname

fname = input("Enter your first name : ")
lname = input("Enter your last name : ")

def printFullName(firstName,lastName):
    print("Your full name is : ",firstName +" "+ lastName)
    
printFullName(fname,lname)
