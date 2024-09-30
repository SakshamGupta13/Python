myList = ["Saksham","Saksham","Gupta"]
# tuple store multiple data
myTuple = ("Saksham","Saksham","Gupta")
# set storer multiple data
mySet = {"Saksham","Saksham","Gupta"}
# dictionary store muultiple data in key value pair
myDict = {"name":"Saksham","email":"abcd@gmail.com","name":"Saksham"}


# access complete data from data set
for data in myList:
    print("list : ",data)
for item in mySet:
    print("set : ",item)
for value in myTuple:
    print("tuple : ",value)
for x in myDict.values():
    print("dict : ",x)
    
# to update the data in all data set
# tuple and set is unchangable
# dict and list is changable
# list, set duplicate item
# set, dict no duplicate item
myList[0] = "AAAA"
print(myList)
myDict[0] = "AAAA"
print(myDict)
# mySet[0] = "AAAA"
# print(mySet)
# myTuple[0] = "AAAA"
# print(myTuple)

# Add new value in data set
myList.append("Mittal")
mySet.add("Mittal")
myDict.update({"name2":"Mittal"})

print("list : ",myList)
print("set : ",mySet)
print("tuple : ",myTuple)
print("dict : ",myDict)

print("----------------")

# to remove the data from data set
myList.pop(0)
mySet.remove("Saksham")
myDict.pop("name")

print("list : ",myList)
print("set : ",mySet)
print("dict : ",myDict)\
    
# convert tuple to list
convertList = list(myTuple)
print(type(convertList))
convertList.append("rohan")
convertList.pop(2)
print(convertList)
myTuple = tuple(convertList)
print(myTuple)