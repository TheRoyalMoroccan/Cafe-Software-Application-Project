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
        [2]: To Add A Beverage To The Beverage List
        [3]: To Alter A Beverage
        [4]: To Delete A Beverage''')

    user_input = int(input('\n\tSelect from the options above: '))

    if user_input == 0:
        main()

    elif user_input == 1:
        print("\n\tHere's The Beverage List\n\t")
        read_product_from_db()
        product()

    elif user_input == 2:
        print('\n\tHere Ts The Beverage List\n\t')
        read_product_from_db()
        new_product = input('\n\tPlease Add A New Beverage To The List : ')
        new_price = float(input('\n\tPlease Enter Desired Price: '))
        write_into_product_db(new_product, new_price)
        print("\n\tYou've Added A Beverage To The List\n\t")
        read_product_from_db()
        product()

    elif user_input == 3:  # Check if input can be change to int & float
        print('\n\tThe Beverage Selections Are: \n\t')
        read_product_from_db()

        product_id = input('Choose Product ID: ')
        product_name = input('Choose A Product Name: ')
        product_price = input('Choose A Product Price: ')

        change_into_product_db(product_name, product_price, product_id)
        print("\n\tYou've Updated The Product's List:\n\t")
        read_product_from_db()
        product()

    elif user_input == 4:
        print('\n\tLets delete a beverage\n\t')
        read_product_from_db()

        deleted_input = int(
            input('\n\tSelected a beverage to be deleted by choosing a number: '))
        delete_product_from_db(deleted_input)

        # whitespace()

        print("\n\tYour Chosen Beverage Has Been Deleted\n\t")
        read_product_from_db()
        product()

    else:
        print('Invalid selection')
        product()


def courier():
    print('\n\tCourier Menu')
    print('''
        [0]: To Return To The Main Menu
        [1]: To View The Current Courier List
        [2]: To Add A Courier To The Courier List
        [3]: To Alter A Courier
        [4]: To Delete A Courier''')

    user_input = int(input('\n\tSelect From The Options Above: '))

    if user_input == 0:
        main()

    elif user_input == 1:
        print("\n\tHere's The Courier's List\n\t")
        read_courier_from_db()
        courier()

    elif user_input == 2:
        print("\n\tHere's The Courier's List\n\t")
        read_courier_from_db()
        courier_name = input('\n\tPlease Add A New Courier : ')
        courier_phone = input('\n\tPlease Enter A Phone Number: ')
        write_into_courier_db(courier_name, courier_phone)
        print("\n\tYou've Added A Courier To The List\n\t")
        read_courier_from_db()
        courier()

    elif user_input == 3:  # Check is\n still needs to be here
        print('\n\tThe Courier List is: ', '\n')
        read_courier_from_db()

        courier_ID = input('Choose A Courier ID: ')
        courier_name = input('Choose A New Courier Name: ')
        courier_number = input('Choose A New Courier Number: ')

        change_into_courier_db(courier_name, courier_number, courier_ID)
        print("\n\tYou've Updated The Courier's List:\n\t")
        read_courier_from_db()
        courier()

    elif user_input == 4:
        print('\n\tLets Delete A Courier')
        read_courier_from_db()
        deleted_input = int(
            input('\n\tChoose A Courier To Be Deleted: '))
        delete_courier_from_db(deleted_input)
        print("\n\tYour Chosen Courier Has Been Deleted:\n\t")
        read_courier_from_db
        courier()
    else:
        print('\n\tInvalid selection')

        courier()


def order():
    print('\n\tOrder Menu')
    print('''
        [0]: To Return To The Main Menu
        [1]: To View The Order List
        [2]: To Add An Order To The List
        [3]: To Update Order Status
        [4]: To Update Existing Order
        [5]: To Delete An Order''')

    user_input = int(input('\n\tSelect From The Options Above: '))

    if user_input == 0:
        main()

    elif user_input == 1:
        print("\n\tHere's The Order's List:")

        for key, value in enumerate(order_list):
            print(f'\n\tOrder Number - {key}{value}')

        order()

    elif user_input == 2:
        customer_name = input('\n\tPlease Enter Your Name : ')
        customer_address = input('\n\tPlease Enter Your Address: ')
        customer_phone_number = int(
            input('\n\tPlease Enter A Phone Number: \n\t'))

        enumerate_orders(product_list)
        product_choice = input(
            '\n\tWhich Product Do You Want Added To Your Order: ')

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

        print("\nYou've Added You're Order: ", new_dict)

        order()

    elif user_input == 3:
        print('\nThe Orders List is: ', '\n')

        for key, value in enumerate(order_list):
            print(f'\n\tOrder Number - {key}{value}')

        order_input = int(
            input('\n\tChoose An Order To Update: '))
        whitespace()
        enumerate_orders(order_status)
        status_input = int(input('\n\tChoose Status To Update: '))

        new_variable = order_list[order_input]
        new_variable['Status'] = order_status[status_input]

        print("\nHere's the new updated beverage menu: ", new_variable)

        order()

    elif user_input == 4:
        print('\n\tLets Update Existing Order\n\t')

        for key, value in enumerate(order_list):
            print(f'\n\tOrder Number - {key}{value}')
        select_order = int(input('\n\tChoose An Order: '))

        chosen_order = order_list[select_order]

        update_dict(chosen_order)
        print("\n\tYou've Updated The Order\n\t")
        for key, value in enumerate(order_list):
            print(f'\n\tOrder Number - {key}{value}')

        order()

    elif user_input == 5:
        print('\nLets Delete An Order')
        for key, value in enumerate(order_list):
            print(f'\n\tOrder Number - {key}{value}')

        deleted_input = int(
            input('\nSelect An Order To Delete: '))

        delete_index(order_list, deleted_input)

        print("You're Order No Longer Exists:\n\t")
        for key, value in enumerate(order_list):
            print(f'\n\tOrder Number - {key}{value}')

        order()
    else:
        print('Invalid selection')
        whitespace()
        order()


main()
