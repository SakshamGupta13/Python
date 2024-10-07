# Error handling or exception handling
# Control over the error in progress

# error in program
# print(x)

# solution
try:
    print(x)
except NameError:
    print("x is not defined" )
    
# 2 error type in python
x = "Saksham"
y = 5
c = x + 5
print(c)