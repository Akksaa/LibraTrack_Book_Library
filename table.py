import mysql.connector as myconn

my_db = myconn.connect( 
    host = "localhost",
    user = "root",
    password = "Aqsa@5112007",
    database = "Book_Library"
)
db_cursor = my_db.cursor()
db_cursor.execute("Create table books(book_id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255) NOT NULL, author VARCHAR(255) NOT NULL, genre VARCHAR(100), publication_year YEAR, is_read BOOLEAN)")

print('table created...')
# db_cursor.execute("Drop table books")

# db_cursor.execute("show tables")

# for i in db_cursor:
#     print(i)
