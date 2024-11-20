from pymongo import MongoClient

# create mongo client connection
client = MongoClient("mongodb://localhost:27017/")

# create new database for todoApp
mydb = client["todoDB"]

# create new collection from database in todoApp
mycol = mydb["taskList"]

# create data using dictionary 
myTask = {"taskName":input("Enter task name : "), "taskDesc":input("Enter task description : "), "taskDate":input("Enter task date : "), "taskStatus":input("Enter task status : ")}

# add data into collection
mycol.insert_one(myTask)

# create friend collection in tododb
myfriendList = mydb["friendList"]

# add friend in friend list
# friend = {"name":"saksham","age":19,"gender":"male"}
friend = [{"name":"saksham","age":19,"gender":"male"},{"name":"daksh","age":20,"gender":"male"},{"name":"mayank","age":20,"gender":"male"}]

# to add friend into collection
# myfriendList.insert_one(friend)
# myfriendList.insert_many(friend)

# delete the data in database
# deleteFriend = {"name":"mayank"}
# myfriendList.delete_one(deleteFriend)

# update the friend list
name = {"name":"saksham gupta"}
myfriendList.update_many({"age":19},{"$set":name})

# get the friend list
friends = myfriendList.find()
for data in friends:
    print(data)