from pymongo import MongoClient

# create connection with mongodb
client = MongoClient("mongodb://localhost:27017")

# create new database in mongodb
mydatabase = client["libdb"]

# create new collection in database
mycollection = mydatabase["addbook"]

# insert data
mybook = {"book":"VAM","rollno":123}
mycollection.insert_one(mybook)