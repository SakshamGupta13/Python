# male -> not entry in 1st compartment
# female -> entry in 1st compartment

userGender = input("Enter your gender(m/f) : ")
if userGender == "m":
    print("You can not sit in metro first compartment")
elif userGender == "f":
    print("You can sit in metro first compartment")
else:
    print("You can sit in any compartment")