products_list = []
with open('Product_list.txt') as load_p_file:
    for load_i in load_p_file:
        products_list.append(load_i.rstrip())


couriers_list = []
with open('Courier_list.txt') as load_c_file:
    for load_w in load_c_file:
        couriers_list.append(load_w.rstrip())


def main():
    option = int(input('''
        To Exit Press 0
        To View Drinks Press 1
        To View Couriers press 2
        Enter your choice here: '''))

    if option == 0:

        with open('Product_list.txt', 'w') as save_p_file:
            for save_i in products_list:
                save_p_file.write(save_i + '\n')

        with open('Courier_list.txt', 'w') as save_c_file:
            for save_w in couriers_list:
                save_c_file.write(save_w + '\n')

        print("\n Goodbye.")
        print("")
        exit()

    elif option == 1:
        product()

    elif option == 2:
        courier()


def product():
    user_input = int(input('''
0: To return to the Main Menu
1: To view the current drinks menu
2: To update existing drinks menu
3: To list & replace a drink
4: To delete a drink
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


def courier():
    user_input = int(input('''
0 To Return To The Main Menu
1 To View The Current Couriers List
2 To Create A New Courier
3 To Updates The Existing Couriers List
4 To Delete A Courier
\tSelect from the options above: '''))

    if user_input == 0:
        main()

    elif user_input == 1:
        print('\nThe courier list is: ', couriers_list)

    elif user_input == 2:
        print('\nThe courier list is: ', couriers_list)
        new_courier = input('\nPlease enter a new courier name: ')
        couriers_list.append(new_courier)
        print("\nYou've added a new courier to the list", couriers_list)

    elif user_input == 3:
        print("\nThe couriers list are: ")
        for value, index in enumerate(couriers_list):
            print(value, index)

        number_input = int(input(
            '\nReplace a courier by selecting the number to associated with the courier:  '))
        new_courier = input('\nTell us a Name to be added')

        couriers_list[number_input] = new_courier
        print("\nHere's the new updated courier list: ", couriers_list)

    elif user_input == 4:
        print('\nLets delete a courier')
        for key, value in enumerate(couriers_list):
            print(key, value)

        deleted_input = int(input(
            '\nSelect a courier to be fired by choosing the number associated with it'))
        del couriers_list[deleted_input]
        print('\nThe new courier list is: ', couriers_list)


main()
