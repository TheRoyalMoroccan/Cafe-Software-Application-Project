import csv
from Functions import read_csv_file, save_list, append_dict, update_dict, delete_index, enumerate_orders, whitespace
from pprint import pprint


order_list = []
product_list = []
courier_list = []
order_status = ['Preparing', 'Quality checks',
                'Driver on the way', 'Delivered']

order_list = read_csv_file('Order_list.csv', order_list)
product_list = read_csv_file('Product_list.csv', product_list)
courier_list = read_csv_file('Courier_list.csv', courier_list)


def main():
    print("\n\tMain Menu")
    print("""
        [0] - To save and exit
        [1] - Product options
        [2] - Courier options
        [3] - Order options""")

    option = int(input("""\n\tEnter your choice here: """))

    if option == 0:
        save_list('Order_list.csv', order_list)
        save_list('Product_list.csv', product_list)
        save_list('Courier_list.csv', courier_list)

        print('\n\tGoodbye')
        exit()

    elif option == 1:
        product()

    elif option == 2:
        courier()

    elif option == 3:
        order()

    else:
        print('Please input a valid input')
        main()


def product():
    print('\n\tProduct options')
    print('''
        [0]: To Return To The Main Menu
        [1]: To View Beverage List
        [2]: To Update Existing Drinks Menu
        [3]: To List & Replace A Drink
        [4]: To Delete A Drink''')

    user_input = int(input('\n\tSelect from the options above: '))

    if user_input == 0:
        main()

    elif user_input == 1:
        print("\n\tHere's The Beverage List\n\t")
        pprint(product_list)

    elif user_input == 2:
        print('\n\tHere Ts The Beverage List\n\t')
        pprint(product_list)

        new_product = input('\n\tPlease Add A New Beverage To The List : ')
        new_price = float(input('\n\tPlease Enter Desired Price: '))

        new_dict = {}
        new_dict['Name'] = new_product
        new_dict['Price'] = new_price
        headers = ['Name', 'Price']

        append_dict('Product_list.csv', new_dict, headers)

        print("\n\tYou've Added A Beverage To The List:", new_dict)

    elif user_input == 3:  # Check is \n still needs to be here
        print('\n\tThe Beverage Selections Are: \n\t')
        enumerate_orders(product_list)

        number_input = float(
            input('\n\tChoose A Number To Replace With Another Beverage: '))
        new_variable = product_list[number_input]
        update_dict(new_variable)

        print("\n\tHere's The Updated Beverage List:\t\n")
        pprint(product_list)
        # product()  # try and fix this

    elif user_input == 4:
        print('\n\tLets delete a beverage\n\t')
        enumerate_orders(product_list)

        deleted_input = int(
            input('\n\tSelected a beverage to be deleted by choosing a number: '))
        whitespace()
        delete_index(product_list, deleted_input)

        print("\n\tYour Chosen Beverage Has Been Deleted\n\t")
        enumerate_orders(product_list)

    else:
        print('Invalid selection')
        product()


def courier():
    print('\n\tCourier Menu')
    print('''
            [0]: To Return To The Main Menu
            [1]: To View The Current Courier List
            [2]: To Add A Courier To The Courier List
            [3]: To Replace A Courier
            [4]: To Delete A Courier''')

    user_input = int(input('\n\tSelect From The Options Above: '))

    if user_input == 0:
        main()

    elif user_input == 1:
        print("\n\tHere's The Courier's List\n\t")
        pprint(courier_list)

    elif user_input == 2:
        print("\n\tHere's The Courier's List\n\t")
        pprint(courier_list)

        courier_name = input('\n\tPlease Add A New Courier : ')
        courier_phone = int(input('\n\tPlease Enter A Phone Number: '))

        new_dict = {}
        new_dict['Name'] = courier_name
        new_dict['Phone Number'] = courier_phone
        headers = ['Name', 'Phone Number']

        append_dict('Courier_list.csv', new_dict, headers)

        print("\n\tYou've added a beverage to the menu:", new_dict)

    elif user_input == 3:  # Check is\n still needs to be here
        print('\nThe Courier List is: ', '\n')

        enumerate_orders(courier_list)
        number_input = int(
            input('\nChoose A Courier To Replace: '))

        new_variable = courier_list[number_input]
        update_dict(new_variable)

        print("\nHere's the new updated beverage menu: ", courier_list)
        product()  # fix this

    elif user_input == 4:
        print('\nLets delete a beverage')
        enumerate_orders(courier_list)

        deleted_input = int(
            input('\nSelected a beverage to be deleted by choosing a number: '))

        delete_index(courier_list, deleted_input)

        print("You've deleted a selection: ", courier_list)
        product()
    else:
        print('Invalid selection')
        product()


def order():
    print('\n\tOrder Menu')
    print('''
            [0]: To Return To The Main Menu
            [1]: To View The Order List
            [2]: To Add An Order List
            [3]: To Replace An Order
            [4]: To Delete An Order''')

    user_input = int(input('\n\tSelect From The Options Above: '))

    if user_input == 0:
        main()

    elif user_input == 1:
        # print("\n\tHere's The Order's List : ", order_list)
        for key, value in enumerate(order_list):
            print(f'\n\tOrder Number - {key}{value}')
    elif user_input == 2:
        customer_name = input('\n\tPlease Enter Your Name : ')
        customer_address = input('\n\tPlease Enter Your Address: ')
        customer_phone_number = int(input('\n\tPlease Enter A Phone Number: '))

        # WHITESPACE
        enumerate_orders(product_list)
        product_choice = input(
            '\n\tWhich Product You Want Added To Your Order: ')

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

        print("\nYou've Added A New Order: ", new_dict)

    elif user_input == 3:  # Check is\n still needs to be here
        print('\nThe Orders List is: ', '\n')

        enumerate_orders(order_list)
        order_input = int(
            input('\nChoose An Order To Update: '))

        enumerate_orders(order_status)
        status_input = int(input('\nChoose Status To Update: '))

        new_variable = order_list[order_input]
        new_variable['Status'] = order_status[order_input]

        print("\nHere's the new updated beverage menu: ", new_variable)

    elif user_input == 4:
        enumerate_orders(order_list)
        select_order = int(input('\nChoose An Order: '))

        chosen_order = order_list[select_order]

        update_dict(chosen_order)
        print(order_list)
        main()

    elif user_input == 5:
        print('\nLets Delete An Order')
        enumerate_orders(order_list)

        deleted_input = int(
            input('\nSelect An Order To Delete: '))

        delete_index(order_list, deleted_input)

        print("You've deleted a selection: ", order_list)
    else:
        print('Invalid selection')
        whitespace()
        product()


main()
