from database import create_table, select_items, insert_data, update_product, delete_products, close_db

welcome = "Welcome to Food App!"


def show_menu():
    menu = """\nPlease select one of the following option:
    1. Add New Table
    2. View all Products
    3. Insert Product
    4. Update Product(s)
    5. Delete Product(s)
    6. Exit
    
    Your selection: """
    num = int(input(menu))

    while num != 6:
        if num == 1:
            create_table()
        elif num == 2:
            select_items()
        elif num == 3:
            insert_data()
        elif num == 4:
            update_product()
        elif num == 5:
            delete_products()
        else:
            print('Invalid Menu Item.')
            return show_menu()
        num = int(input(menu))


print(welcome)
show_menu()

print('\nHave a nice day!')
close_db()
