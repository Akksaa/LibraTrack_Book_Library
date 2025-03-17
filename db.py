import mysql.connector as myconn

my_db = myconn.connect( 
    host = "localhost",
    user = "root",
    password = "Aqsa@5112007",
)

db_cursor = my_db.cursor()
db_cursor.execute("Create database Book_Library")

print("database created...")