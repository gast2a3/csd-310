#Importing mysql.connector and errorcode
import mysql.connector
from mysql.connector import errorcode
from pymongo import MongoClient
#Establishing the connection to MongoDB
connect=MongoClient('mongodb+srv://admin:admin@cluster0.za5b2oe.mongodb.net/?retryWrites=true&w=majority')
#Creating/Using the "pytech" database
db=connect["pytech"]
#Building the config database object
config = {
    "user": "pysports_user",
    "password": "!QAZ1qaz@WSX2wsx",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}
#Establishing the connection and Displaying connection responses/errors
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

