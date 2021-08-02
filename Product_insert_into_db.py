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
sql = 'INSERT INTO Products (Product_Name, Product_Price) VALUES (%s, %s)'
val = [('Latte', 2.5),
       ('Cappuccino', 1.25),
       ('Tea', 2.5),
       ('Espresso', 1.5),
       ('Americano', 1.25),
       ('Black', 2.0),
       ('Flat White', 2.0),
       ('Mocha', 2.25),
       ('Frappe', 3.50),
       ('Ice Tea', 4.50),
       ('Caramel Frappucino', 3.50)
       ]
cursor.executemany(sql, val)

connection.commit()
cursor.close()
connection.close()
