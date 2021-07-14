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
    0: To Return To The Main Menu
    1: To View The Current Drinks Menu
    2: To Update Existing Drinks Menu
    3: To List & Replace A Drink
    4: To Delete A Drink
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
        print("\n The Courier List Is : ", couriers_list)

    elif user_input == 2:
        print("\nThe Courier List Is : ", couriers_list)
        new_couriers = input("\n Please Enter A New Courier Name : ")
        couriers_list.append(new_couriers)
        print("\n You Have Created A New Courier")
        print(couriers_list)

    elif user_input == 3:
        for value, index in enumerate(couriers_list):
            print(value, index)
        courier_index_value = int(
            input("\n Please Enter The Index value Of The courier You Want To Update : "))
        new_courier_name = input(
            "\n Please Enter A New Name For The Courier: ")
        couriers_list[courier_index_value] = new_courier_name
        print(couriers_list)

    elif user_input == 4:
        print("\n", [list((i, couriers_list[i]))
              for i in range(len(couriers_list))])
        delete_courier_index_value = int(
            input("\n Please Enter The Index value Of The Courier You Want To Delete : "))
        del products_list[delete_courier_index_value]
        print("\n The New Courier List Is :", couriers_list)


main()
