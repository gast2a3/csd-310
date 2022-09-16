from pymongo import MongoClient
connection=MongoClient('mongodb+srv://admin:admin@cluster0.za5b2oe.mongodb.net/?retryWrites=true&w=majority')
pytechdatabase=connection["pytech"]
studentCollection=pytechdatabase["students"]
print("The student is:")
print(studentCollection.find_one({"student_id": 1008}))
