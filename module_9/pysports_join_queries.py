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
    "user": "root",
    "password": "!QAZ1qaz@WSX2wsx",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}
#Establishing the connection and Displaying connection responses/errors
try:
    db = mysql.connector.connect(**config)
    
    cursor = db.cursor()
#SELECT query from team table
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")
#Getting Cursor results
    players = cursor.fetchall()
    print("\n -- DISPLAYING PLAYER RECORDS --")
#For loop to format results
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))
    input("\n\n Press any key to continue... ")
#Handle errors
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)
