#Importing mysql.connector and errorcode
from imghdr import what
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
#Establishing the connection and Displaying connection responses/errors
db = mysql.connector.connect(**config)    
cursor = db.cursor()

#^^^^All above is standard copy/paste w/ minor adjustment^^^^

#Defining the commands in the Program
class whatabook:#Define whatabook menu as a class for easy recall
    def show_menu():#Building the Main Menu
        print("\n**********THIS IS WHATABOOK**********\n" +
        "\n---Main Menu---\n\n1: View Books\n2: View Store Locations\n3: My Account\n4: Exit Program\n")


    def show_books(_cursor):#Building the Show Books Menu w/ Inner Join Query
        _cursor.execute("SELECT book_id, book_name, author, details FROM book;")
        books = _cursor.fetchall()
        print("\n ----DISPLAYING BOOKS----")
        for book in books:
            print("\n Book ID: {},\n Book Name: {}\n Author: {}\n Details: {}\n".format(book[0], book[1], book[2], book[3]))
        input("Press any key to continue...")

    def show_locations(_cursor):#Building the Locations Menu 
        _cursor.execute("SELECT store_id, locale FROM store;")
        locations = _cursor.fetchall()
        print("\n----DISPLAYING LOCATIONS----")
        for location in locations:
            print("\n Store ID: {},\n Locale: {}\n".format(location[0], location[1]))
        input("Press any key to continue...")


    def validate_user():#Building the user validation loop
        try:
            user_id = int(input("\nEnter your User ID (Example '1' for User ID 1)  "))
            if user_id <1 or user_id >3:
                print("\n Incorrect User ID")
                whatabook.validate_user()
            return user_id
        except ValueError:
            print("\n Incorrect input format, please try again.")
            whatabook.validate_user()

    def show_account_menu():#Building the User Account Menu
        try:
            print("\n----User Menu----")
            print("\n1. Wishlist\n2. Add Book\n3. Main Menu\n")
            user_choice = int(input("Choose what you would like to do (Example '1' for Wishlist)  "))
            if user_choice <1 or user_choice >3:
                print("\n Incorrect menu option. Please try again.")
                whatabook.show_account_menu()
            return user_choice
        except ValueError:
            print("\n Incorrect input format, please try again.")
            whatabook.show_account_menu()

    def show_wishlist(_cursor, _user_id):#Building Wishlist Query
        _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN book ON wishlist.book_id = book.book_id WHERE user.user_id = {}".format(_user_id))
        wishlist = _cursor.fetchall()
        print("\n----DISPLAYING WISHLIST----")
        for user in wishlist:
            print("\n User ID: {}\n First Name: {}\n Last Name: {}".format(user[0], user[1], user[2]))
        for book in wishlist:
            print(input(" Book ID: {},\n Book Name: {}\n Author: {}\n".format(book[3], book[4], book[5]) + "\nPress any key to continue..."))
            return whatabook.show_account_menu()

    def show_books_to_add(_cursor, _user_id):#Building Books to be added to Wishlist
        inquire_books = ("SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
        _cursor.execute(inquire_books)
        adding_books = _cursor.fetchall()
        print("\n---DISPLAYING THE BOOKS YOU CAN ADD---")
        for book in adding_books:
            print("\n Book ID: {}\n Book Name: {}\n Author: {}\n Details: {}".format(book[0], book[1], book[2], book[3]))
        
    def add_book_to_wishlist(_cursor, _user_id, _book_id):
        add_book = ("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))
        _cursor.execute(add_book)


#Navigation Commands
while True:
    try:
        whatabook.show_menu()
        menu_choice = int(input("What do you want to do? "))
        if menu_choice == 1:
            whatabook.show_books(cursor)
        elif menu_choice == 2:
            whatabook.show_locations(cursor)
        elif menu_choice == 3:
            user_id = whatabook.validate_user()
            user_option = whatabook.show_account_menu()
            if user_option == 1:
                whatabook.show_wishlist(cursor, user_id)
            elif user_option == 2:
                whatabook.show_books_to_add(cursor, user_id)
                book_id = int(input("\nPlease choose a Book ID to add:  "))
                whatabook.add_book_to_wishlist(cursor, user_id, book_id)
                db.commit()
                added_book = input("Added book to your wishlist. Press any key to continue...")
                user_option = whatabook.show_account_menu()
            elif user_option == 3:
                whatabook.show_menu()
            elif user_option <1 or user_option >3:
                print("\n Incorrect option, please try again.\n")
        elif menu_choice == 4:
            print("Thank you....")
            exit()
        elif menu_choice <1 or menu_choice >4:
                print("\nIncorrect input, please try again.\n")
    except ValueError:
        print("\nIncorrect input format, please try again.")
            



#Handle Errors
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(" The supplied username or password are invalid")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(" The specified database does not exist")
        else:
            print(err)
