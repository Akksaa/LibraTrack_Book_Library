import mysql.connector as myconn
import pandas as pd
from config import DATABASE_HOST, DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USER


my_db = myconn.connect( 
    host = DATABASE_HOST,
    user = DATABASE_USER,
    password = DATABASE_PASSWORD,
    database = DATABASE_NAME
)

db_cursor = my_db.cursor()

# def get_all_books():
#     db_cursor.execute("select * from books")
#     results = db_cursor.fetchall()
#     cols = ["id", "title", "author", "genre", "publication_year", "is_read"]
#     # print(pd.DataFrame(results, columns=["id", "title", "author", "genre", "publication_year", "is_read"]))
#     print("from get_all_books():",len(results))
#     if results:
#         return pd.DataFrame(results, columns=cols)
#     return pd.DataFrame()

# result = get_all_books()
# print(result)

def get_all_books():
    try:
        db_cursor.execute("select * from books")
        results = db_cursor.fetchall()
        cols = ["id", "title", "author", "genre", "publication_year", "is_read"]
        
        if results:
            return pd.DataFrame(results, columns=cols)
        return pd.DataFrame()
    except Exception as e:
        print(f"Error in get_all_books: {e}")
        return pd.DataFrame()