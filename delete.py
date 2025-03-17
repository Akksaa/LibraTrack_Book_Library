import mysql.connector as myconn

from select2 import get_all_books

my_db = myconn.connect( 
    host = "localhost",
    user = "root",
    password = "Aqsa@5112007",
    database = "Book_Library"
)

db_cursor = my_db.cursor()

def delete_book(title):
    sql = "delete from books where title=%s"
    val = (title,)

    db_cursor.execute(sql,val)
    my_db.commit()
    result = get_all_books()
    print(result)

    print("Item Deleted!")
    return result