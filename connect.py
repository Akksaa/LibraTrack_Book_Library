import mysql.connector as myconn

my_db = myconn.connect( 
    host = "localhost",
    user = "root",
    password = "Aqsa@5112007",
)

print(my_db, "connection established...")