import mysql.connector as myconn
import pandas as pd

my_db = myconn.connect( 
    host = "localhost",
    user = "root",
    password = "Aqsa@5112007",
    database = "Book_Library"
)

db_cursor = my_db.cursor()

def get_all_books():
    db_cursor.execute("select * from books")
    results = db_cursor.fetchall()
    cols = ["id", "title", "author", "genre", "publication_year", "is_read"]
    # print(pd.DataFrame(results, columns=["id", "title", "author", "genre", "publication_year", "is_read"]))
    print("from get_all_books():",len(results))
    if results:
        return pd.DataFrame(results, columns=cols)
    return pd.DataFrame()

result = get_all_books()
print(result)