# list in python -> list can contain duplicate item
# list can store multiple data
myList = ["Saksham","Daksh","Gupta"]
# tuple store multiple data
myTuple = ("Saksham","Daksh","Gupta")
# set storer multiple data -> no duplicate item
mySet = {"Saksham","Daksh","Gupta"}
# dictionary store muultiple data in key value pair -> no duplicate item
myDict = {"name":"Saksham","email":"abcd@gmail.com"}


# to check the datatype of all above data set
print("list : ",type(myList),"tuple : ",type(myTuple))
print("set : ",type(mySet),"dict : ",type(myDict))

# how to identify list,set,tuple,dictionary
# list -> [], tuple -> (), set -> {}, dict -> {:}

# example of data set
# myData = {"Saksham","Daksh","Gupta"}  # set
# myGroup = ("Saksham","Daksh","Gupta")  # tuple
# myClass = ["Saksham","Daksh","Gupta"]  # list
# myFriends = {"name":"Saksham","Age":19}  # dictionary

print("------------------------")
# access data from data set
print("list : ",myList[0])
print("set : ",mySet)
print("tuple : ",myTuple[1])
print("dict : ",myDict["name"])

print("--=-=-=-=-=-=-")

# access complete data from data set
for data in myList:
    print("list : ",data)
for item in mySet:
    print("set : ",item)
for value in myTuple:
    print("tuple : ",value)
for x in myDict.values():
    print("dict : ",x)