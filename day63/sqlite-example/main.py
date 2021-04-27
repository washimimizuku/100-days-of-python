import os
import sqlite3


LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
DATABASE_FILE = os.path.join(LOCATION, "books-collection.db")

db = sqlite3.connect(DATABASE_FILE)
cursor = db.cursor()

# Create table
cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title VARCHAR(250) NOT NULL UNIQUE, author VARCHAR(250) NOT NULL, rating FLOAT NOT NULL)")

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
