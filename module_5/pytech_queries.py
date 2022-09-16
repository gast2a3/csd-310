from pymongo import MongoClient
connection=MongoClient('mongodb+srv://admin:admin@cluster0.za5b2oe.mongodb.net/?retryWrites=true&w=majority')
pytechdatabase=connection["pytech"]
studentCollection=pytechdatabase["students"]
print("DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY:")
print(studentCollection.find_one({"student_id": 1008}))

print("DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY:")
for document in studentCollection.find():
    print(document)
