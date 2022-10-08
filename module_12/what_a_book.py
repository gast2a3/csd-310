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
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "whatabook",
    "raise_on_warnings": True
}
#Defining the commands in the Program
def show_menu():#Building the Main Menu
    print("\n**********THIS IS WHATABOOK**********" +
    "\n---Main Menu---\n\n1: View Books\n2: View Store Locations\n3: My Account\n4: Exit Program\n")
    while(True):
        try:
            menuInput = int(input("What would you like to do? (Select a menu number)\n"))
            if menuInput <1 or menuInput >4:
                print("Incorrect selection, please try again.\n")
            return menuInput
            break
        except ValueError:
            print("Incorrect input format, please try again.")

def show_books(_cursor):#Building the Show Books Menu w/ Inner Join Query
    _cursor.execute("SELECT book_id, book_name, author, details FROM book;")
    books = _cursor.fetchall()
    print("\n ---DISPLAYING BOOKS---")
    for book in books:
        print("\n Book Name: {}\n Author: {}\n Details: {}\n".format(book[0], book[1], book[2]))

def show_locations(_cursor):#Building the Locations Menu 
    _cursor.execute("SELECT store_id, locale FROM store;")
    locations = _cursor.fetchall()
    print("\n---DISPLAYING LOCATIONS---")
    for location in locations:
        print("\n Locale: {}\n".format(location[1]))

def validate_user():#Building the user validation loop
    try:
        user_id = int(input("\nEnter your User ID (Example '1' for User ID 1)  "))
        if user_id <1 or user_id >3:
            print("\n Incorrect User ID")
        return user_id
    except ValueError:
        print("\n Incorrect input format, please try again.")

def show_account_menu():#Building the User Account Menu w/ loop
    try:
        print("\n---User Menu---")
        print("\n1. Wishlist\n2. Add Book\n3. Main Menu\n")
        user_choice = int(input("Choose what you would like to do (Example '1' for Wishlist)  "))
        return user_choice
    except ValueError:
        print("\n Incorrect input format, please try again.")

def show_wishlist(_cursor, _user_id):#Building Wishlist Query
    _cursor.execute("SELECT user.user_id, user.first_name, user. last_name, book.book_id, book.book_name, book.author FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN book ON wishlist.book_id = book.book_id WHERE user.user_id = {}".format(_user_id))
    wishlist = _cursor.fetchall()
    print("\n---DISPLAYING WISHLIST---")
    for book in wishlist:
        print("\n Book Name: {}\n Author: {}\n".format(book[4], book[5]))

def show_books_to_add(_cursor, _user_id):#Building Books to be added to Wishlist w/ loop
    query_books = ("SELECT book_id, book_name, author, details " +
                    "FROM book " +
                    "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    print(query_books)
    _cursor.execute(query_books)
    adding_books = _cursor.fetchall()
    print("\n---DISPLAYING THE BOOKS YOU CAN ADD---")
    for book in adding_books:
        print("\n Book ID: {}\n Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) " +
                    "VALUES({}, {})".format(_user_id, _book_id))

#Establishing the connection and Displaying connection responses/errors
try:
    db = mysql.connector.connect(**config)    
    cursor = db.cursor()

#Navigation Commands
    menu_choice = show_menu()
    if menu_choice == 1:
        show_books(cursor)
    if menu_choice == 2:
        show_locations(cursor)
    if menu_choice == 3:
        user_id = validate_user()
        user_option = show_account_menu()
        if user_option == 1:
            show_wishlist(cursor, user_id)
        elif user_option == 2:
            add_book_to_wishlist(cursor, user_id)
#ADD the book menu..............
        elif user_option == 3:
            show_menu()
    menu_choice = show_menu()######MENU crashes at this point. Keep t/s######
    ##########################################################################

#Handle Errors
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)
