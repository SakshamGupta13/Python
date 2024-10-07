# oops in python

# object oriented programming -> object

# class -> it is a container which is collectection of variables and function
# example -> saksham class
# saksham.fullname = "ahshdbdkj"
# saksham.age = 19
# saksham.sleeping()
# saksham.eating()
# saksham.watching()

# class syntax
class ClassName:
    print("This is my class")
    
class Saksham:
    age = 19
    fullName = "Saksham Gupta"
    email = "sakksham@gmail.com"
    
    def pocketMoney(this,amount):
        print("My pocket money is ",amount)
        
    def salary(this):
        amt = int(input("Enter salary of 1 day : "))
        amt = amt * 31
        print("Monthly salary is : ",amt)
        
# create class object
# object:className = ClassName()
s:Saksham = Saksham()
print("My name is ",s.fullName," , age : ",s.age)
s.pocketMoney(15000)
s.salary()