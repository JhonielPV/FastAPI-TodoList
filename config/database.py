from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:1234@cluster0.aa6dgwg.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db

collection_name = db['todo_collection']
 