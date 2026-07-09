from pymongo import MongoClient

# Local MongoDB
client = MongoClient("mongodb://localhost:27017/")

# MongoDB Atlas Example
# client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/")
db = client["mydatabase"]           # create or access a database
collection = db["mycollection"]     # create or access a collection
data = {"name": "Farhan", "age": 23}
collection.insert_one(data)

# Insert multiple documents
collection.insert_many([
    {"name": "Ali", "age": 25},
    {"name": "Sara", "age": 21}
])
# Find one
result = collection.find_one({"name": "Farhan"})
print(result)

# Find all
for doc in collection.find():
    print(doc)
collection.update_one(
    {"name": "Farhan"},
    {"$set": {"age": 24}}
)
collection.delete_one({"name": "Farhan"})
collection.delete_many({"age": {"$lt": 25}})
# Greater than
collection.find({"age": {"$gt": 20}})

# AND condition
collection.find({"name": "Ali", "age": 25})

# OR condition
from pymongo import ASCENDING
collection.find({"$or": [{"name": "Ali"}, {"age": 23}]})
# Create index
collection.create_index([("name", ASCENDING)])

# Sort by age
for doc in collection.find().sort("age"):
    print(doc)
