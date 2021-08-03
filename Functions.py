import csv
import pymysql
import os
from dotenv import load_dotenv
from prompt_toolkit import print_formatted_text, HTML


def read_csv_file(file_name, csv_to_read):
    with open(file_name, 'r') as csv_file:
        csv_to_read = csv.DictReader(csv_file)
        csv_list = []
        for row in csv_to_read:
            csv_list.append(row)
        return csv_list


def save_list(file_name, list_name):
    with open(file_name, "w", newline='') as updated:
        if list_name:
            writer = csv.DictWriter(updated, fieldnames=list_name[0].keys())
            writer.writeheader()
            writer.writerows(list_name)


def print_csv_file(file_name, csv_file):
    with open(file_name, 'r') as csv_print:
        csv_file = csv.DictReader(csv_print)
        for row in csv_file:
            print(dict(row))


def append_dict(file_name, dict_of_elem, field_names):
    with open(file_name, 'a+', newline='') as write_obj:
        dict_writer = csv.DictWriter(write_obj, fieldnames=field_names)
        dict_writer.writerow(dict_of_elem)


def update_dict(chosen_item):
    for key, value in chosen_item.items():

        chosen_value = input(
            f'\nThe {key} Category Has Value Of {value}. Enter New Value For {key}: ')

        if chosen_value == '':
            chosen_item[key] = value
            print_formatted_text(
                HTML('\n\t<i><ansicyan>Nothing has been changed</ansicyan></i>'))
        else:
            chosen_item[key] = chosen_value


def delete_index(list_name, deleted_input):
    del list_name[deleted_input]


def enumerate_orders(order_goes_here):
    for key, value in enumerate(order_goes_here):
        print(key, value)


def whitespace():
    print('\n')


def read_courier_from_db():

    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )

    cursor = connection.cursor()

    cursor.execute(
        'SELECT Courier_Id, Courier_Name, Courier_Phone FROM Couriers')

    rows = cursor.fetchall()
    for row in rows:
        print(
            f"\n Courier's ID: {int(row[0])}, Courier's Name: {str(row[1])}, Courier's Phone Number: {row[2]}")

    cursor.close()
    connection.close()


def read_product_from_db():

    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )

    cursor = connection.cursor()

    cursor.execute(
        'SELECT Product_Id, Product_Name, Product_Price FROM Products')

    rows = cursor.fetchall()
    for row in rows:
        print(
            f"\n Product ID: {int(row[0])}, Product Name: {str(row[1])}, Product Price: {float(row[2])}")

    cursor.close()
    connection.close()


def write_into_courier_db(new_courier, new_number):
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )

    cursor = connection.cursor()

    sql = 'INSERT INTO Couriers (Courier_Name, Courier_Phone) VALUES (%s, %s)'
    val = [(new_courier, new_number)]
    cursor.executemany(sql, val)

    connection.commit()
    cursor.close()
    connection.close()


def write_into_product_db(new_product, new_price):
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )

    cursor = connection.cursor()

    sql = 'INSERT INTO Products (Product_Name, Product_Price) VALUES (%s, %s)'
    val = [(new_product, new_price)]
    cursor.executemany(sql, val)

    connection.commit()
    cursor.close()
    connection.close()


def delete_product_from_db(deleted_product_id):
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )

    cursor = connection.cursor()
    sql = 'DELETE FROM Products WHERE Product_Id = %s'
    val = [(deleted_product_id)]

    cursor.execute(sql, val)

    connection.commit()
    cursor.close()
    connection.close()


def delete_courier_from_db(deleted_product_id):
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )

    cursor = connection.cursor()
    sql = 'DELETE FROM Couriers WHERE Courier_Id = %s'
    val = [(deleted_product_id)]

    cursor.execute(sql, val)

    connection.commit()
    cursor.close()
    connection.close()


def change_into_product_db(new_product, new_price, product_id):
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )

    cursor = connection.cursor()

    if new_product or new_price:
        sql = 'UPDATE Products SET'

        if new_product and new_price:
            sql += ' Product_Name = %s, Product_Price = %s WHERE Product_Id = %s'
            val = (new_product, new_price, product_id)
            print_formatted_text(HTML(
                "\n\t<i><ansimagenta>You've Updated Both Product Name And Price</ansimagenta></i>"))

        elif new_product:
            sql += ' Product_Name = %s WHERE Product_Id = %s'
            val = (new_product, product_id)
            print_formatted_text(HTML(
                "\n\t<i><ansimagenta>You've Updated The Product Name</ansimagenta></i>"))
            print_formatted_text(HTML(
                "\n\t<i><ansimagenta>You've Left The Product Price As It Is</ansimagenta></i>"))

        elif new_price:
            sql += ' Product_Price = %s WHERE Product_Id = %s'
            val = (new_price, product_id)
            print_formatted_text(HTML(
                "\n\t<i><ansimagenta>You've Updated The Product Price</ansimagenta></i>"))
            print_formatted_text(HTML(
                "\n\t<i><ansimagenta>You've Left The Updated Product Name As It Is</ansimagenta></i>"))

        cursor.execute(sql, val)
        connection.commit()
    else:
        print_formatted_text(
            HTML("\n\t<i><ansimagenta>You've Changed Nothing</ansimagenta></i>"))

    cursor.close()
    connection.close()


def change_into_courier_db(new_courier, new_number, courier_id):
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )

    cursor = connection.cursor()

    if new_courier or new_number:
        sql = 'UPDATE Couriers SET'

        if new_courier and new_number:
            sql += ' Courier_Name = %s, Courier_Phone = %s WHERE Courier_Id = %s'
            val = (new_courier, new_number, courier_id)
            print_formatted_text(HTML(
                "\n\t<i><ansiyellow>You've Updated Both Courier Name And Number</ansiyellow></i>"))

        elif new_courier:
            sql += ' Courier_Name = %s WHERE Courier_Id = %s'
            val = (new_courier, courier_id)
            print_formatted_text(
                HTML("\n\t<i><ansiyellow>You've Updated The Courier Name</ansiyellow></i>"))
            print_formatted_text(
                HTML("\n\t<i><ansiyellow>You've Left The Courier Number As It Is</ansiyellow></i>"))

        elif new_number:
            sql += ' Courier_Phone = %s WHERE Courier_Id= %s'
            val = (new_number, courier_id)
            print_formatted_text(HTML(
                "\n\t<i><ansiyellow>You've Updated The Courier Number</ansiyellow></i>"))
            print_formatted_text(HTML(
                "\n\t<i><ansiyellow>You've Left The Courier Name As It Is</ansiyellow></i>"))

        cursor.execute(sql, val)
        connection.commit()
    else:
        print_formatted_text(
            HTML("\n\t<i><ansiyellow>You've Changed Nothing</ansiyellow></i>"))

    cursor.close()
    connection.close()
