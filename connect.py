import os
import mysql.connector as myconn

from config import DATABASE_HOST, DATABASE_PASSWORD, DATABASE_USER


# my_db = myconn.connect( 
#     host = DATABASE_HOST,
#     user = DATABASE_USER,
#     password = DATABASE_PASSWORD,
# )

my_db = myconn.connect(
    host=os.getenv("DATABASE_HOST"),
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
)


print(my_db, "connection established...")