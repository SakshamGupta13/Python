# Job

userAge = int(input("Enter your age : "))
userGender = input("Enter your gender(m/f) : ")
if userAge > 18:
    if userGender == "m":
        print("You can apply for private job")
    elif userGender == "f":
        print("Ypu can apply for government job")
    else:
        print("There is no opening")
else:
    print("You are under age")
    


# userGender = input("Enter your gender(m/f) : ")
# userAge = int(input("Enter your age : "))
# if userGender == "m" and userAge > 18:
#     print("You can apply for private job")
# elif userGender == "f" and userAge > 18:
#     print("Ypu can apply for government job")
# else:
#     print("You are not eligible for job")