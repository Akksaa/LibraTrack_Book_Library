import mysql.connector as myconn
from config import DATABASE_HOST, DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USER


from select2 import get_all_books

my_db = myconn.connect( 
    host = DATABASE_HOST,
    user = DATABASE_USER,
    password = DATABASE_PASSWORD,
    database = DATABASE_NAME
)

db_cursor = my_db.cursor()

def add_book(title, author, genre, publication_year, is_read):
    sql = "INSERT INTO books(title, author, genre, publication_year, is_read) VALUES ( %s, %s, %s, %s, %s)"
    val = (title, author, genre, publication_year, is_read)

    db_cursor.execute(sql, val)
    my_db.commit()
    print(db_cursor.rowcount, "Record Inserted...")
    books = get_all_books()
    print("from insert.py",books)

    return books