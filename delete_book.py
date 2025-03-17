import mysql.connector as myconn
import pandas as pd
from config import DATABASE_HOST, DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USER
from select2 import get_all_books

my_db = myconn.connect( 
    host = DATABASE_HOST,
    user = DATABASE_USER,
    password = DATABASE_PASSWORD,
    database = DATABASE_NAME
)

db_cursor = my_db.cursor()

# def delete_book_from_lib(title):
#     sql = "delete from books where title=%s"
#     val = (title,)

#     db_cursor.execute(sql,val)
#     my_db.commit()
#     result = get_all_books()
#     print(result)

#     print("Item Deleted!")

def delete_book_from_lib(title):
    try:
        sql = "delete from books where title=%s"
        val = (title,)
        db_cursor.execute(sql, val)
        my_db.commit()
        result = get_all_books()
        print(result)
        print("Item Deleted!")
        return result
    except Exception as e:
        print(f"Error in delete_book_from_lib: {e}")
        return pd.DataFrame()
