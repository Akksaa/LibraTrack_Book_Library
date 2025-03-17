import mysql.connector as myconn
from config import DATABASE_HOST, DATABASE_PASSWORD, DATABASE_USER

my_db = myconn.connect( 
    host = DATABASE_HOST,
    user = DATABASE_USER,
    password = DATABASE_PASSWORD,
)

db_cursor = my_db.cursor()
db_cursor.execute("Create database Book_Library")

print("database created...")