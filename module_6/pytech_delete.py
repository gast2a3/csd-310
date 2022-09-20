from pymongo import MongoClient
def delete_one():
    connection=MongoClient('mongodb+srv://admin:admin@cluster0.za5b2oe.mongodb.net/?retryWrites=true&w=majority')
    pytechdatabase=connection["pytech"]
    studentCollection=pytechdatabase["students"]
    print("\n DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY:\n")
    for document in studentCollection.find():
        print(document)
    Student10 = {"first_name": "George", "last_name": "Harrison", "student_id": 1010}
    #Establishing the code to combine the collection
    Student10_student_id = studentCollection.insert_one(Student10).inserted_id
    print("\n-- INSERT STATEMENTS --")
    print("Inserted student record into the students collection with document_id" + str(Student10_student_id))
    print("\n-- DISPLAYING STUDENT TEST DOC --")
    print(studentCollection.find_one({"student_id": 1010}))
    myQuery = {"first_name": "George"}
    studentCollection.delete_one(myQuery)
    print("\n DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY:\n")
    for document in studentCollection.find():
        print(document)
    print("\nEnd of program, press any key to continue...\n")
delete_one()
