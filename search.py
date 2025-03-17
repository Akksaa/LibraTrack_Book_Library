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

def search_books(query, field):

    sql = f"SELECT * FROM books WHERE {field.lower()} LIKE %s"
    parameters = (f"%{query}%",)
    
    results = db_cursor.execute(sql, parameters)
    print("from search",results)
    if results:
        return pd.DataFrame(results)
    return pd.DataFrame()
