products_list = ['Latte', 'Cappuccino', 'Tea', 'Espresso', 'Americano']


def main():
    option = int(input('''
        To Exit press 0
        To Enter press 1
        Enter your choice here: '''))

    if option == 0:
        print("\n Goodbye.")
        print("")
        exit()

    elif option == 1:
        product()


def product():
    user_input = int(input('''
    0: To return to the Main Menu
    1: To view the current drinks menu
    2: To update existing drinks menu
    3: To list & replace a drink
    4: To delete a drink
    \tSelect from the options above: '''))

    if user_input == 0:
        main()

    elif user_input == 1:
        print("\n The Product List Is : ", products_list)

    elif user_input == 2:
        print("\nThe Product List Is : ", products_list)
        new_product = input("\n Please Enter A New Product Name : ")
        products_list.append(new_product)
        print("\n You Have Created A New Product")
        print(products_list)

    elif user_input == 3:
        for value, index in enumerate(products_list):
            print(value, index)
        product_index_value = int(
            input("\n Please Enter The Index value Of The Product You Want To Update : "))
        new_product_name = input(
            "\n Please Enter A New Product Name For The Product: ")
        products_list[product_index_value] = new_product_name
        print(products_list)

    elif user_input == 4:
        print("\n", [list((i, products_list[i]))
              for i in range(len(products_list))])
        delete_product_index_value = int(
            input("\n Please Enter The Index value Of The Product You Want To Delete : "))
        del products_list[delete_product_index_value]
        print("\n The New Product List Is :", products_list)


main()
