# list can store data, data can be different types int,float
# listt can store the duplicate data
# list ia an orderd data set -> sorting ascending or descending

# create list and store your friends name
friendList = ["Daksh","Saksham","Mukesh"]

# print the list of friend names
print(friendList)

# add the age of  your friend into list
# append will add the data into end of the list
friendList.append(11)
friendList.append(22)
print(friendList)

# add the data using index number
friendList.insert(0,"Mayank")
print(friendList)

friendList.insert(3,"Gupta")
print(friendList)

# to acceess the data using index numbeer
# print(friendList[2])

# to delete the data from list
# friendList.remove("Mukesh")
# print(friendList)
# friendList.remove("Saksham")
# print(friendList)

# access the complete list
# for name in friendList:
#     print(name)

# pop will delete the data using index
friendList.pop(2)
friendList.pop(0)
print(friendList)