from pymongo import MongoClient
def delete_one():
    connection=MongoClient('mongodb+srv://admin:admin@cluster0.za5b2oe.mongodb.net/?retryWrites=true&w=majority')
    pytechdatabase=connection["pytech"]
    studentCollection=pytechdatabase["students"]
    print("\n DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY:\n")
    for document in studentCollection.find():
        print(document)
    myQuery = {"first_name": "John"}
    studentCollection.delete_one(myQuery)
    print(document)
delete_one()
