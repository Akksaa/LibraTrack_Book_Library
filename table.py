import mysql.connector as myconn
from config import DATABASE_HOST, DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USER


my_db = myconn.connect( 
    host = DATABASE_HOST,
    user = DATABASE_USER,
    password = DATABASE_PASSWORD,
    database = DATABASE_NAME
)

db_cursor = my_db.cursor()
db_cursor.execute("Create table books(book_id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255) NOT NULL, author VARCHAR(255) NOT NULL, genre VARCHAR(100), publication_year YEAR, is_read BOOLEAN)")

print('table created...')
# db_cursor.execute("Drop table books")

# db_cursor.execute("show tables")

# for i in db_cursor:
#     print(i)
