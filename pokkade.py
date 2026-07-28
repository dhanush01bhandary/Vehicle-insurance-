from pymongo import MongoClient

client = MongoClient("mongodb+srv://dhanush01bhandary_db_user:UjkeLI49xKyGQh1B@cluster0.tkp8cl7.mongodb.net/?appName=Cluster0")

print(client.list_database_names())

db = client["Proj1"]
print(db.list_collection_names())

collection = db["Proj1_Data"]

print("Document count:", collection.count_documents({}))

doc = collection.find_one()
print(doc)