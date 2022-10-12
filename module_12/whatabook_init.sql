CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

CREATE TABLE store (
    store_id    INT NOT NULL    AUTO_INCREMENT,
    locale  VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

INSERT INTO store(locale)
    VALUES('123 Mountain St, ID 83647');

INSERT INTO book(book_name, author, details)
    VALUES('Game Walkthroughs', 'Rico Suave', 'This book will walk you through many games step-by-step.');

INSERT INTO book(book_name, author, details)
    VALUES('Making Tacos', 'Javier Ortega', 'This book will teach you everything to make perfect tacos everytime.');

INSERT INTO book(book_name, author, details)
    VALUES('Intro to Python', 'John Smith', 'This book will teach you the beginning steps to writing your own Python code.');

INSERT INTO book(book_name, author, details)
    VALUES('Making Bread', 'Jane Austin', 'This book will teach you all the steps and techniques for making many types of bread.');

INSERT INTO book(book_name, author, details)
    VALUES('Homemade Beer', 'Elton John', 'This book will teach you what equipment and techniques you need to brew your own beer.');

INSERT INTO book(book_name, author, details)
    VALUES('How to Build a Computer', 'Jean-Luc Picard', 'This book will teach you how to build a computer like a pro!');

INSERT INTO book(book_name, author, details)
    VALUES('Mixing Drinks', 'Morgan Freeman', 'This book will teach you all the bar techniques to impress your friends!');

INSERT INTO book(book_name, author, details)
    VALUES('Wood Working', 'Harry Styles', 'This book will teach you what you need to know so you can build anything you want with wood.');

INSERT INTO book(book_name, author, details)
    VALUES('Hunting Techniques', 'Harry Potter', 'This book will teach you how to successfully bag anything you hunt.');

INSERT INTO user(first_name, last_name) 
    VALUES('Samuel', 'Jackson');

INSERT INTO user(first_name, last_name)
    VALUES('Harry', 'Styles');

INSERT INTO user(first_name, last_name)
    VALUES('Chris', 'Pratt');

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Samuel'), 
        (SELECT book_id FROM book WHERE book_name = 'Homemade Beer')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Harry'),
        (SELECT book_id FROM book WHERE book_name = 'How to Build a Computer')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Chris'),
        (SELECT book_id FROM book WHERE book_name = 'Making Tacos')
    );