import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host,
    user,
    password,
    database
)

# A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
cursor = connection.cursor()

# Add code here to insert a new record
sql = 'INSERT INTO Couriers (Courier_Name, Courier_Phone) VALUES (%s, %s)'
val = [('David', '+447 5821 71134'),
       ('Muhammed', '+447 7097 79632'),
       ('Adam', '+447 4162 73936'),
       ('Moosa', '+447 1068 90286'),
       ('John', '+447 1619 60340'),
       ('Rumaanah', '+447 3520 12767'),
       ('Idris', '+447 4578 53374'),
       ('Oussama', '+447 4574 66901')
       ]
cursor.executemany(sql, val)

connection.commit()
cursor.close()
connection.close()
