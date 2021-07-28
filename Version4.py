import csv
from Functions import read_csv_file, save_list, append_dict, update_dict, delete_index, whitespace


order_list = []
products_list = []
courier_list = []
order_status = ['Preparing', 'Quality checks',
                'Driver on the way', 'Delivered']

orders_list = read_csv_file('Order_list.csv', order_list)
products_list = read_csv_file('Product_list.csv', products_list)
couriers_list = read_csv_file('Courier_list.csv', courier_list)


def main():
    print("\n\tMain Menu")
    print("""
        [0] - To save and exit
        [1] - Product options
        [2] - Courier options
        [3] - Order details
    """)

    option = int(input("""\n\tEnter your choice here: """))

    if option == 0:
        save_list('Order_list.csv', orders_list)
        save_list('Product_list.csv', products_list)
        save_list('Courier_list.csv', couriers_list)

        print('Goodbye')
        exit()

    elif option == 1:
        print(products_list)

    # elif option == 2:
    # courier()

    # elif option == 3:
    #     order()


def product():
    print('\n\tProduct options')
    print('''
            [0]: To return to the Main Menu
            [1]: To view the current drinks menu
            [2]: To update existing drinks menu
            [3]: To list & replace a drink
            [4]: To delete a drink''')
    user_input = int(input('\n\tSelect from the options above: '))

    if user_input == 0:
        main()

    elif user_input == 1:
        print('\nHere is the beverage menu : ', products_list)

    elif user_input == 2:
        print('\nHere is the beverage menu : ', products_list)

        new_product = input('\nPlease add a new beverage to the menu : ')
        new_price = float(input('\nPlease enter desired price: '))
        new_dict = {}
        new_dict['Name'] = new_product
        new_dict['Price'] = new_price
        headers = ['Name', 'Price']
        append_dict('Product_list.csv', new_dict, headers)

        print("\nYou've added a beverage to the menu:", new_dict)

    elif user_input == 3:
        print('\nThe beverage selections are: ', '\n')
        for key, value in enumerate(products_list):
            print(key, value)

        number_input = int(
            input('\nChoose a beverage by selecting the number to replace with your desired beverage: '))
        new_variable = products_list[number_input]
        update_dict(new_variable)

        print("\nHere's the new updated beverage menu: ", products_list)
        main()

    elif user_input == 4:
        print('\nLets delete a beverage')
        for key, value in enumerate(products_list):
            print(key, value)

        deleted_input = int(
            input('\nSelected a beverage to be deleted by choosing a number: '))
        delete_index(products_list, deleted_input)

        print(products_list)

        # del products_list[deleted_input]
        # print('\nThe new beverage menu is: ', products_list)


main()
