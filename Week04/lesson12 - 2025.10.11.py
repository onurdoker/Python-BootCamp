"""
What is a Database and Why is it Necessary?

What is it?
A database is an organized collection of data.
Just like a library organized its books, databased organize information.

Why is it Necessary?
It is needed to store information permanently - such as user data, product lists, or notes - that we don't want to lose when our program closes.

What is SQLite?
SQLite is a lightweight, serverless database engine that stores the entire database in a single file.
It is very easy to use with Python and requires no installation.
"""

import sqlite3

# ! First Example
# link = sqlite3.connect('links.db')

# * Once a connection is established, we should close it after we are done
# link.close()

# ! Second Example
# link = sqlite3.connect("library.db")
# cursor = link.cursor()
# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS books
#                (
#                    id
#                    INTEGER
#                    PRIMARY
#                    KEY
#                    AUTOINCREMENT,
#                    name
#                    TEXT,
#                    authors
#                    TEXT
#                )
#                """)

# * We need to commit on order to save the changes made
# link.commit()
#
# link.close()

# ! Third Example
"""
Basic Database Operations

In general, we can perform four main operations on databases.
CRUD (Create, Read, Update, Delete) represents the four fundamental operations of a database application.

Operation           Meaning                 SQLCommand
Create              Add data                INSERT
Read                Retrieve data           SELECT
Update              Update data             UPDATE
Delete              Delete data             DELETE
"""

# link = sqlite3.connect("library.db")
# cursor = link.cursor()

# * Inserting new data
# cursor.execute(
#     "INSERT INTO books VALUES(NULL, ?, ?)",
#     ("The Lords of the Rings",
#      "Tolkien"),
#     )
#
# link.commit()
# link.close()

# ! Fourth Example
# * We can modify the data entry process so that data can be entered from the outside (by the user)
# link = sqlite3.connect("library.db")
# cursor = link.cursor()
#
# book_name = input("Enter book name: ")
# book_author = input("Enter book author: ")
#
# cursor.execute(
#     "INSERT INTO books VALUES(NULL, ?, ?)",
#     (book_name,
#      book_author),
#     )
#
# link.commit()
# link.close()

# ! Fifth Example
# * Reading data
# link = sqlite3.connect("library.db")
# cursor = link.cursor()
#
# cursor.execute(
#     "SELECT * FROM books",
#     )
#
# books = cursor.fetchall()  # response list
#
# for book in books:
#     print(f"Book id: {book[0]}, Book Title: {book[1]}, Authors: {book[2]}")
#
# link.commit()
# link.close()

# ! Sixth Example
# * Update data
# link = sqlite3.connect("library.db")
# cursor = link.cursor()
#
# cursor.execute(
#     "UPDATE books SET name=? WHERE id=?",
#     ("Hobbit",
#      1),
#     )
#
# link.commit()
# link.close()

# ! Seventh Example
# link = sqlite3.connect("library.db")
# cursor = link.cursor()
#
# cursor.execute(
#     "SELECT * FROM books",
#     )
#
# books = cursor.fetchall()  # response list
#
# for book in books:
#     print(f"Book id: {book[0]}, Book Title: {book[1]}, Authors: {book[2]}")
#
# book_id = int(input("Please enter the ID of book to be updated: "))
# book_name = input("Please enter the name of the book to be updated: ")
#
# cursor.execute(
#     "UPDATE books SET name=? WHERE id=?",
#     (book_name,
#      book_id),
#     )
#
# link.commit()
# link.close()

# ! Eighth Example
# * Deleting Data
# link = sqlite3.connect("library.db")
# cursor = link.cursor()
#
# cursor.execute(
#     "DELETE FROM books WHERE id = ?",
#     (1,),
#     )
#
# link.commit()
# link.close()


# ! Nineth Example
# link = sqlite3.connect("library.db")
# cursor = link.cursor()
#
# cursor.execute(
#     "SELECT name FROM books",
#     )
#
# books = cursor.fetchall()
# print(books)
#
# link.commit()
# link.close()

# ! Tenth Example

# def list_books():
#     link = sqlite3.connect("library.db")
#     cursor = link.cursor()
#
#     cursor.execute(
#         "SELECT * FROM books",
#         )
#
#     books = cursor.fetchall()  # response list
#
#     for book in books:
#         print(f"Book id: {book[0]}, Book Title: {book[1]}, Authors: {book[2]}")
#
#     if len(books) > 0:
#         return True
#     else:
#         print("No books found to list")
#         return False
#
# def add_book():
#     link = sqlite3.connect("library.db")
#     cursor = link.cursor()
#
#     book_name = input("Enter book name: ")
#     book_author = input("Enter book author: ")
#
#     cursor.execute(
#         "INSERT INTO books VALUES(NULL, ?, ?)",
#         (book_name,
#          book_author),
#         )
#
#     link.commit()
#     link.close()
#     print(f"{book_name} has been added to database.")
#
# def update_book():
#     list_info = list_books()
#
#     if list_info:
#         link = sqlite3.connect("library.db")
#         cursor = link.cursor()
#
#         book_id = int(input("Please enter the ID of book to be updated: "))
#         book_name = input("Please enter the name of the book to be updated: ")
#
#         cursor.execute(
#             "UPDATE books SET name=? WHERE id=?",
#             (book_name,
#              book_id),
#             )
#
#         link.commit()
#         link.close()
#     else:
#         print("No books found to update.")
#
# def delete_book():
#     list_info = list_books()
#
#     if list_info:
#         link = sqlite3.connect("library.db")
#         cursor = link.cursor()
#
#         cursor.execute(
#             "DELETE FROM books WHERE id = ?",
#             (1,),
#             )
#
#         link.commit()
#         link.close()
#     else:
#         print(f"No books found to delete.")
#
# def program():
#     while True:
#
#         print("Welcome to Library Database"
#               "\nPlease select the operation you would like to perform:"
#               "\n1- List the books"
#               "\n2- Add a book"
#               "\n3- Update a book"
#               "\n4- Delete a book"
#               "\n5- Exit")
#
#         operation = int(input("Please enter your choice: "))
#
#         match operation:
#             case 1:
#                 list_books()
#             case 2:
#                 add_book()
#             case 3:
#                 update_book()
#             case 4:
#                 delete_book()
#             case 5:
#                 break
#             case _:
#                 print("That is not a valid choice.")
#
# if __name__ == "__main__":
#     program()

# ! Eleventh Example
# * SQLAlchemy
"""
SQLAlchemy, allows you to perform all database operations using Python objects and classes, almost completely eliminating the need to write SQL 
manually.
"""

"""
Library Management with SQLAlchemy ORM

1. What is ORM?
ORM (Object-Relational Mapping Operations) means mapping objects to relational data.

Purpose: To create a bridge between the classes and objects you write in Python (object-oriented side) and the tables and rows in a relational 
database (relational side).

Benefits: Instead of writing raw SQL commands (such as SELECT, INSERT, UPDATE, DELETE) you can perform database operations as if you were working 
with normal Python objects.

This makes your code more secure, readable, and database-independent.
"""
from sqlalchemy import (create_engine,
                        Column,
                        Integer,
                        String)
from sqlalchemy.orm import (sessionmaker,
                            declarative_base)

# * Connecting Database
engine = create_engine("sqlite:///library_orm.db")

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer,
                primary_key=True)
    name = Column(String)
    author = Column(String)

    def __repr__(self):
        return f"Book(id={self.id}, name ={self.name}, Author={self.author}"

Base.metadata.create_all(engine)

# * Adding book
# book1 = Book(name='Think Python',
#              author="O'Riley")
#
# session.add(book1)
# session.commit()

# * Adding multidata
# book2 = Book(name='C#',
#              author="Mustafa Hoca")
# book3 = Book(name='JavaScript Lessons',
#              author="O'Riley")
# session.add_all([book2,
#                  book3])
# session.commit()

# * Printing books
# all_books = session.query(Book).all()
# print(type(all_books),
#       all_books)
#
# for book in all_books:
#     print(book.name)

# * Filtering
# filtered_books = session.query(Book).filter(Book.author == "Mustafa Hoca").all()
# print(filtered_books)

# * Updating
# updated_books = session.query(Book).filter(Book.id == 2).first()
# updated_books.name = "C++"
# session.commit()

# * Deleting
# deleted_books = session.query(Book).filter(Book.id == 4).first()
# session.delete(deleted_books)
# session.commit()
#
# books = session.query(Book).all()
# print(books)
