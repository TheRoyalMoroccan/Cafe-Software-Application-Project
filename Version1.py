products_list = ['Latte', 'Cappuccino', 'Tea', 'Espresso', 'Americano']


def main():
    option = int(input('''
[0] To Exit press
[1] To Enter press
\nEnter your choice here: '''))

    if option == 0:
        print("\n Goodbye.")
        exit()

    elif option == 1:
        product()


def product():
    user_input = int(input('''
[0] To return to the Main Menu
[1] To view the current drinks menu
[2] To update existing drinks menu
[3] To list & replace a drink
[4] To delete a drink
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
