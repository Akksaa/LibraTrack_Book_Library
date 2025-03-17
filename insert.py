import mysql.connector as myconn

from select2 import get_all_books

my_db = myconn.connect( 
    host = "localhost",
    user = "root",
    password = "Aqsa@5112007",
    database = "Book_Library"
)

db_cursor = my_db.cursor()

# title = input("Book title:")
# author = input("author:")
# genre = input("genre:")
# publication_year = int(input("Publication Year:"))

def add_book(title, author, genre, publication_year, is_read):
    sql = "INSERT INTO books(title, author, genre, publication_year, is_read) VALUES ( %s, %s, %s, %s, %s)"
    val = (title, author, genre, publication_year, is_read)

    db_cursor.execute(sql, val)
    my_db.commit()
    print(db_cursor.rowcount, "Record Inserted...")
    books = get_all_books()
    print("from insert.py",books)

    return books