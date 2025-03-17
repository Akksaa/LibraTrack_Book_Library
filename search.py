import mysql.connector as myconn
import pandas as pd

my_db = myconn.connect( 
    host = "localhost",
    user = "root",
    password = "Aqsa@5112007",
    database = "Book_Library"
)

db_cursor = my_db.cursor()

def search_books(query, field):

    sql = f"SELECT * FROM books WHERE {field.lower()} LIKE %s"
    parameters = (f"%{query}%",)
    
    results = db_cursor.execute(sql, parameters)
    print("from search",results)
    if results:
        return pd.DataFrame(results)
    return pd.DataFrame()
