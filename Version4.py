import csv
from Functions import read_csv_file

order_status = ['Preparing', 'Quality checks',
                'Driver on the way', 'Delivered']

order_list = {}
courier_list = {}
products_list = {}

read_csv_file('Product_list.csv', products_list)
read_csv_file('Order_list.csv', order_list)
read_csv_file('Courier_list.csv', courier_list)


def main():
    print("""\033[33m\n\tMain Menu:\033[0m""")
    print("""
        [0] - To Exit
        [1] - Product Options
        [2] - Courier Options
        [3] - Order Details
    """)

    option = int(input("""Enter your choice here: """))

    if option == 0:
        print('Goodbye')
        exit()

    elif option == 1:
        product()

    # elif option == 2:
    #     courier()

    # elif option == 3:
    #     order()


def product():
    print('\n\tProduct options')
    user_input = int(input('''
            [0]: To return to the Main Menu
            [1]: To view the current drinks menu
            [2]: To update existing drinks menu
            [3]: To list & replace a drink
            [4]: To delete a drink
    \nSelect from the options above: '''))

    if user_input == 0:
        main()

    elif user_input == 1:
        print('\nHere is the beverage menu : ', products_list)

    elif user_input == 2:
        print('\nHere is the beverage menu : ', products_list)
        new_product = input('\nPlease add a new beverage to the menu : ')
        products_list.append(new_product)
        print("\nYou've added a beverage to the menu:", products_list)

    elif user_input == 3:
        print('\nThe beverage selections are: ', '\n')
        for key, value in enumerate(products_list):
            print(key, value)

        number_input = int(
            input('\nChoose a beverage by selecting the number to replace with your desired beverage: '))
        new_product = input('\nTell us your desired beverage: ')

        products_list[number_input] = new_product
        print("\nHere's the new updated beverage menu: ", products_list)

    elif user_input == 4:
        print('\nLets delete a beverage')
        for key, value in enumerate(products_list):
            print(key, value)

        deleted_input = int(
            input('\nSelected a beverage to be deleted by choosing a number: '))
        del products_list[deleted_input]
        print('\nThe new beverage menu is: ', products_list)


main()
