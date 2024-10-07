# error 1
# print(x)     # -> gives error

# error handling
try:
    print(x)
except NameError:
    print("x is not defined")
    
    
# error 2
# y = 1/0

# error handling
try:
    y = 1/0
except ZeroDivisionError:
    print("divide by zero")
    
    
# error 3
name = "Saksham"
# n = int(name)

# error handling
try:
    n = int(name)
except ValueError:
    print("value error")
    
    
# error 4
friends = ["Saksham","Daksh","Mukesh"]
# friends[4]

# error handling
try:
    friends[4]
except IndexError:
    print("You are calling wrong index")
    

# error 5
amount = 500
email = "support@gmail.com"
# total = amount + email

# error handling
try:
    total = amount + email
except TypeError:
    print("type error")
