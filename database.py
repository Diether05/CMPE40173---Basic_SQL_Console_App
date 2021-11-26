# creating a python SQL application
import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('foodapp.db')
cur = conn.cursor()


# close database connection
def close_db():
    conn.close()


# select everything from table
def select_items():
    print('Tables: ')
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")  # get all the table in the schema
    print(cur.fetchall())

    question = input('\nWould you like to see data? ')

    if question.lower() == 'yes':
        name = input('Select a table name: ')
        try:
            cur.execute("SELECT * FROM {}".format(name))
            rows = cur.fetchall()
            print('\nID\t|\tProduct\t|\tPrice\t|\tStock\t|\tCategory')

            for i in range(len(rows)):
                row = str(rows[i]).split(',')
                print(row[0] + '\t ' + row[1] + '\t' + row[2] + '\t ' + row[3] + '\t' + row[4])
            input("\nPress any key to continue...")


        except Error as e:
            print(e)
            return select_items()
    elif question.lower() == 'no':
        print('\nOk!')
    else:
        print('\nInvalid response (looking for yes or no)\n')
        return select_items()


# create a new table if it doesn't exist
def create_table():
    table = input('Enter a table name: ')

    try:
        cur.execute("CREATE TABLE {} (id TEXT PRIMARY KEY,product TEXT,price REAL,stock INTEGER, category TEXT);"
                    .format(table))
    except Error as e:
        print(e)
        return create_table()
    conn.commit()


# insert a new product into table
def insert_data():
    print('\nTables: ')
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cur.fetchall())

    insert = True
    while insert:
        question = input('\nWould you like to add an item to a table?: ')

        if question.lower() == 'yes':
            table = input('Enter a table: ')
            idd = input('Enter a product id: ')
            product = input('Enter a product name: ')
            price = int(input('Enter a price: '))
            stock = int(input('Enter the stock: '))
            category = input('Enter a product category: ')
            try:
                cur.execute('INSERT INTO {}(id,product,price,stock,category) VALUES ("{}","{}",{},{},"{}")'
                            .format(table, idd, product, price, stock, category))
            except Error as e:
                print(e)
                return insert_data()
        elif question.lower() == 'no':
            print('\nOk!')
            insert = False
        else:
            print('\nInvalid response (looking for yes or no)\n')
            return insert_data()
    conn.commit()


# delete a product from the database
def delete_products():
    print('\nTables: ')
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cur.fetchall())

    question = input('Would You Like to Delete a Product?: ')

    if question.lower() == 'yes':
        name = input('\nChoose the Table of the Product: ')
        idd = input('ID of the product: ')

        try:
            cur.execute('DELETE FROM {} where id= "{}"'.format(name, idd))
            print('Product Deleted\n')
            input("\nPress any key to continue...")
            conn.commit()
        except Error as e:
            print(e)
            return delete_products()
    elif question.lower() == 'no':
        print('\nOk!')
    else:
        print('\nInvalid response (looking for yes or no)\n')
        return delete_products()


# update product from the table
def update_product():
    print('\nTables: ')
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cur.fetchall())

    question = input('Would You Like to Update a Product?: ')

    if question.lower() == 'yes':
        table = input('Choose a Table to Update From: ')
        idd = input('Choose a Product ID to Update: ')

        try:
            cur.execute('SELECT * FROM {} WHERE id = "{}"'.format(table, idd))
            rows = list(cur.fetchall())
            print('Name \t | \t Price \t | \t Stock')

            for i in range(len(rows)):
                row = str(rows[i]).split(',')
                print(row[0] + '\t ' + row[1] + '\t' + row[2] + '\t ' + row[3] + '\t' + row[4])


            if (len(rows)) == 0:
                print('\nInvalid Item.\n')
                return update_product()

            else:
                price = int(input('Price: '))
                stock = int(input('Stock: '))
                cur.execute("UPDATE {} SET price = {} ,stock = {}  WHERE id ='{}'"
                            .format(table, price, stock, idd))
                conn.commit()

                cur.execute('SELECT * FROM {} WHERE id = "{}"'.format(table, idd))
                rows = list(cur.fetchall())
                for i in range(len(rows)):
                    row = str(rows[i]).split(',')
                    print(row[0] + '\t ' + row[1] + '\t' + row[2] + '\t ' + row[3] + '\t' + row[4])
                    input("\nPress any key to continue...")
        except Error as e:
            print(e)
            return update_product()

    elif question.lower() == 'no':
        print('\nOk!')
    else:
        print('\nInvalid response (looking for yes or no)\n')
        return update_product()
