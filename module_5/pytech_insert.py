#Importing pymongo and MongoClient
from pymongo import MongoClient
#Defining "insert_one()" command
def insert_one():
    #Establishing the connection to MongoDB
    connect=MongoClient('mongodb+srv://admin:admin@cluster0.za5b2oe.mongodb.net/?retryWrites=true&w=majority')
    #Creating/Using the "pytech" database
    db=connect["pytech"]
    #Creating/Using the "students" collection
    collection=db["students"]
    #Creating the entries for the collection
    Student1 = {"first_name": "John", "last_name": "Lennon", "student_id": 1007}
    Student2 = {"first_name": "Paul", "last_name": "McCartney", "student_id": 1008}
    Student3 = {"first_name": "Ringo", "last_name": "Starr", "student_id": 1009}
    #Establishing the code to combine the collection
    Student1_student_id = collection.insert_one(Student1).inserted_id
    Student2_student_id = collection.insert_one(Student2).inserted_id
    Student3_student_id = collection.insert_one(Student3).inserted_id
    #Printing the completed actions
    print("Inserted student record into the students collection with document_id" + str(Student1_student_id))
    print("Inserted student record into the students collection with document_id" + str(Student2_student_id))
    print("Inserted student record into the students collection with document_id" + str(Student3_student_id))
    print("""
End of program, press any key to continue...""")
insert_one()
