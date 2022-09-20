from pymongo import MongoClient
connection=MongoClient('mongodb+srv://admin:admin@cluster0.za5b2oe.mongodb.net/?retryWrites=true&w=majority')
pytechdatabase=connection["pytech"]
studentCollection=pytechdatabase["students"]
update = studentCollection.update_one({"student_id": 1007}, {"$set": {"last_name": "Smith"}})
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
print(studentCollection.find_one({"student_id": 1007}))
