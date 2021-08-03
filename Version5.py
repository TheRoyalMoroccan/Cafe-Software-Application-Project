import time
from prompt_toolkit import print_formatted_text, HTML
from Functions import read_csv_file, save_list, append_dict, update_dict, delete_index, enumerate_orders, whitespace
from Functions import read_courier_from_db, read_product_from_db, write_into_product_db, write_into_courier_db, delete_product_from_db, delete_courier_from_db, change_into_product_db, change_into_courier_db


order_list = []
product_list = []
courier_list = []
order_status = ['Preparing', 'Quality checks',
                'Driver on the way', 'Delivered']

order_list = read_csv_file('Order_list.csv', order_list)
product_list = read_csv_file('Product_list.csv', product_list)
courier_list = read_csv_file('Courier_list.csv', courier_list)


def greetings():

    print_formatted_text(
        HTML('''\n\t<b><ansiwhite>VERY</ansiwhite></b>\n\t'''))
    time.sleep(0.5)
    print_formatted_text(
        HTML('''\n\t<b><ansired>         VERY</ansired></b>\n\t'''))
    time.sleep(0.5)
    print_formatted_text(
        HTML('''\n\t<b><ansigreen>                  NICE...</ansigreen></b>\n\t'''))
    time.sleep(1.5)
    print_formatted_text(
        HTML('''\n\t<b><ansimagenta>ONE</ansimagenta></b>\n\t'''))
    time.sleep(0.5)
    print_formatted_text(
        HTML('''\n\t<b><ansiyellow>        POUND</ansiyellow></b>\n\t'''))
    time.sleep(0.5)
    print_formatted_text(
        HTML('''\n\t<b><ansiblue>                  FISH...</ansiblue></b>\n\t'''))
    time.sleep(0.5)
    print_formatted_text(
        HTML('''\n\t<b><ansicyan>         CAFE</ansicyan></b>\n\t'''))
    time.sleep(2.0)


def main():
    greetings()
    print_formatted_text(
        HTML('\n\t<b><u><ansiwhite>Main Menu</ansiwhite></u></b>'))
    print("""
        [0] - To Save And Exit
        [1] - Product Options
        [2] - Courier Options
        [3] - Order Options""")

    option = int(input("""\n\tEnter your choice here: """))

    if option == 0:
        save_list('Order_list.csv', order_list)
        save_list('Product_list.csv', product_list)
        save_list('Courier_list.csv', courier_list)

        print_formatted_text(
            HTML('\n\t<i><ansiwhite>Goodbye</ansiwhite></i>'))
        exit()

    elif option == 1:
        whitespace()
        product()

    elif option == 2:
        whitespace()
        courier()

    elif option == 3:
        whitespace()
        order()

    else:
        print_formatted_text(
            HTML('\n\t<i><ansiwhite>Invalid Input, Please Try Again</ansiwhite></i>'))
        whitespace()
        main()


def product():
    print_formatted_text(
        HTML('\n\t<b><u><ansimagenta>Product options</ansimagenta></u></b>'))
    print('''
        [0]: To Return To The Main Menu
        [1]: To View Beverage List
        [2]: To Add A Beverage To The Beverage List
        [3]: To Alter A Beverage
        [4]: To Delete A Beverage''')

    user_input = int(input('\n\tSelect from the options above: '))
    whitespace()

    if user_input == 0:
        main()

    elif user_input == 1:
        print_formatted_text(
            HTML("\n\t<b><u><ansimagenta>Beverage List</ansimagenta></u></b>"))
        read_product_from_db()
        whitespace()
        product()

    elif user_input == 2:
        print_formatted_text(
            HTML("\n\t<b><u><ansimagenta>Beverage List</ansimagenta></u></b>"))
        read_product_from_db()
        new_product = input('\n\tPlease Add A New Beverage To The List: ')
        new_price = float(input('\n\tPlease Enter Desired Price: '))
        write_into_product_db(new_product, new_price)
        whitespace()
        print_formatted_text(
            HTML("\n\t<b><u><ansimagenta>Beverage List</ansimagenta></u></b>"))
        read_product_from_db()
        print_formatted_text(HTML(
            "\n\t<i><ansimagenta>You've Added A Beverage To The List</ansimagenta></i>"))
        whitespace()
        product()

    elif user_input == 3:  # Check if input can be change to int & float
        print_formatted_text(
            HTML('\n\t<b><u><ansimagenta>Beverage List</ansimagenta></u></b>'))
        read_product_from_db()

        product_id = input('\n\tChoose Product ID: ')
        product_name = input('\n\tChoose A Product Name: ')
        product_price = input('\n\tChoose A Product Price: ')

        change_into_product_db(product_name, product_price, product_id)

        whitespace()
        print_formatted_text(
            HTML("\n\t<b><u><ansimagenta>Beverage List</ansimagenta></u></b>"))
        read_product_from_db()
        print_formatted_text(
            HTML("\n\t<i><ansimagenta>Beverage List Updated</ansimagenta></i>"))
        whitespace()
        product()

    elif user_input == 4:
        print_formatted_text(
            HTML('\n\t<b><u><ansimagenta>Beverage List</ansimagenta></u></b>'))
        read_product_from_db()

        deleted_input = int(
            input('\n\tSelect A Beverage To Be Deleted: '))
        delete_product_from_db(deleted_input)
        whitespace()
        print_formatted_text(
            HTML('\n\t<b><u><ansimagenta>Beverage List</ansimagenta></u></b>'))
        read_product_from_db()
        print_formatted_text(
            HTML("\n\t<i><ansimagenta>Beverage Has Been Deleted</ansimagenta></i>"))
        whitespace()
        product()

    else:
        whitespace()
        print_formatted_text(
            HTML('\n\t<i><ansimagenta>Invalid Input, Please Try Again</ansimagenta></i>'))
        whitespace()
        product()


def courier():
    print_formatted_text(
        HTML('\n\t<b><u><ansiyellow>Courier Menu</ansiyellow></u></b>'))
    print('''
        [0]: To Return To The Main Menu
        [1]: To View The Current Courier List
        [2]: To Add A Courier To The Courier List
        [3]: To Alter A Courier
        [4]: To Delete A Courier''')

    user_input = int(input('\n\tSelect From The Options Above: '))
    whitespace()

    if user_input == 0:
        main()

    elif user_input == 1:
        print_formatted_text(
            HTML("\n\t<b><u><ansiyellow>Courier List</ansiyellow></u></b>"))
        read_courier_from_db()
        whitespace()
        courier()

    elif user_input == 2:
        print_formatted_text(
            HTML("\n\t<b><u><ansiyellow>Courier List</ansiyellow></u></b>"))
        read_courier_from_db()
        courier_name = input('\n\tPlease Add A New Courier : ')
        courier_phone = input('\n\tPlease Enter A Phone Number: ')
        write_into_courier_db(courier_name, courier_phone)
        whitespace()
        print_formatted_text(
            HTML("\n\t<b><u><ansiyellow>Courier List</ansiyellow></u></b>"))
        read_courier_from_db()
        print_formatted_text(HTML(
            "\n\t<i><ansiyellow>You've Added A Courier To The List</ansiyellow></i>"))
        whitespace()
        courier()

    elif user_input == 3:  # See if you can put int & float
        print_formatted_text(
            HTML("\n\t<b><u><ansiyellow>Courier List</ansiyellow></u></b>"))
        read_courier_from_db()

        courier_ID = input('\n\tChoose A Courier ID: ')
        courier_name = input('\n\tChoose A New Courier Name: ')
        courier_number = input('\n\tChoose A New Courier Number: ')

        change_into_courier_db(courier_name, courier_number, courier_ID)

        whitespace()
        print_formatted_text(
            HTML("\n\t<b><u><ansiyellow>Courier List</ansiyellow></u></b>"))
        read_courier_from_db()
        print_formatted_text(HTML(
            "\n\t<i><ansiyellow>Courier List Updated</ansiyellow></i>"))
        whitespace()
        courier()

    elif user_input == 4:
        print_formatted_text(
            HTML("\n\t<b><u><ansiyellow>Courier List</ansiyellow></u></b>"))
        read_courier_from_db()
        deleted_input = int(
            input('\n\tSelect A Courier To Be Deleted: '))
        delete_courier_from_db(deleted_input)
        whitespace()
        print_formatted_text(
            HTML("\n\t<b><u><ansiyellow>Courier List</ansiyellow></u></b>"))
        read_courier_from_db()
        print_formatted_text(HTML(
            "\n\t<i><ansiyellow>Courier Has Been Deleted</ansiyellow></i>"))
        whitespace()
        courier()

    else:
        whitespace()
        print_formatted_text(
            HTML('\n\t<i><ansiyellow>Invalid Input, Please Try Again</ansiyellow></i>'))
        whitespace()
        courier()


def order():
    print_formatted_text(
        HTML('\n\t<b><u><ansicyan>Courier Menu</ansicyan></u></b>'))
    print('''
        [0]: To Return To The Main Menu
        [1]: To View The Order List
        [2]: To Add An Order To The List
        [3]: To Update Order Status
        [4]: To Update Existing Order
        [5]: To Delete An Order''')

    user_input = int(input('\n\tSelect From The Options Above: '))
    whitespace()

    if user_input == 0:
        main()

    elif user_input == 1:
        print_formatted_text(
            HTML("\n\t<b><u><ansicyan>Order List</ansicyan></u></b>\n\t"))

        for key, value in enumerate(order_list):
            print(f'Order Number - {key}{value}\n\t')
        whitespace()
        order()

    elif user_input == 2:
        print_formatted_text(
            HTML("\n\t<b><u><ansicyan>Insert Customer Information</ansicyan></u></b>\n\t"))

        customer_name = input('\n\tPlease Enter Your Name: ')
        customer_address = input('\n\tPlease Enter Your Address: ')
        customer_phone_number = int(
            input('\n\tPlease Enter A Phone Number: '))

        whitespace()

        enumerate_orders(product_list)
        product_choice = input(
            '\n\tWhich Product Do You Want Added To Your Order: ')
        whitespace()
        enumerate_orders(courier_list)
        courier_choice = int(
            input('\n\tPlease Choose A Courier To Deliver Your Order: '))

        new_dict = {}
        new_dict['Customer name'] = customer_name
        new_dict['Customer address'] = customer_address
        new_dict['Customer phone'] = customer_phone_number
        new_dict['Courier'] = courier_choice
        new_dict['Status'] = order_status[0]
        new_dict['Items'] = product_choice

        headers = ['Customer name', 'Customer address',
                   'Customer phone', 'Courier', 'Status', 'Items']

        append_dict('Order_list.csv', new_dict, headers)

        print_formatted_text(
            HTML("\n\t<i><ansicyan>You've Added An Order</ansicyan></i>\n\t"))
        print_formatted_text(
            HTML("\n\t<i><ansicyan>New Order</ansicyan></i>"))
        print(new_dict)

        whitespace()
        order()

    elif user_input == 3:
        print_formatted_text(
            HTML("\n\t<b><u><ansicyan>Order List</ansicyan></u></b>\n\t"))

        for key, value in enumerate(order_list):
            print(f'Order Number - {key}{value}\n\t')

        order_input = int(
            input('\n\tChoose An Order To Update: '))
        whitespace()
        enumerate_orders(order_status)
        status_input = int(input('\n\tChoose Status To Update: '))

        new_variable = order_list[order_input]
        new_variable['Status'] = order_status[status_input]

        print_formatted_text(
            HTML("\n\t<i><ansicyan>Order Status Updated</ansicyan></i>\n\t"))
        print_formatted_text(
            HTML("\n\t<i><ansicyan>Updated Order</ansicyan></i>"))
        print(new_variable)

        whitespace()
        order()

    elif user_input == 4:
        print_formatted_text(
            HTML("\n\t<b><u><ansicyan>Order List</ansicyan></u></b>\n\t"))

        for key, value in enumerate(order_list):
            print(f'Order Number - {key}{value}\n\t')
        select_order = int(input('\n\tChoose An Order: '))

        chosen_order = order_list[select_order]

        update_dict(chosen_order)
        whitespace()
        print_formatted_text(
            HTML("\n\t<b><u><ansicyan>Order List</ansicyan></u></b>"))
        for key, value in enumerate(order_list):
            print(f'Order Number - {key}{value}\n\t')
        print_formatted_text(
            HTML("\n\t<i><ansicyan>Updated The Order</ansicyan></i>"))
        whitespace()
        order()

    elif user_input == 5:
        print_formatted_text(
            HTML("\n\t<b><u><ansicyan>Order List</ansicyan></u></b>\n\t"))
        for key, value in enumerate(order_list):
            print(f'Order Number - {key}{value}\n\t')

        deleted_input = int(
            input('\n\tSelect An Order To Delete: '))

        delete_index(order_list, deleted_input)

        print_formatted_text(
            HTML("\n\t<b><u><ansicyan>Order List</ansicyan></u></b>\n\t"))
        for key, value in enumerate(order_list):
            print(f'Order Number - {key}{value}\n\t')
        print_formatted_text(
            HTML("\n\t<i><ansicyan>Order Deleted</ansicyan></i>"))

        whitespace()

        order()
    else:
        print('Invalid selection')
        whitespace()
        order()


main()
