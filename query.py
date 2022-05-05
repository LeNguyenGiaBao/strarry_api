import mysql.connector as connector

def connect():
    connection = connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="strarry"
    )
    return connection

def signup_controller(user):
    try:
        connection =connect()
        cursor = connection.cursor()
        query = 'insert into account (email, password) values (%s, %s)'
        value = (user.email, user.password)

        cursor.execute(query, value)
        connection.commit()
        return cursor.lastrowid
    
    except connector.Error as error:
        print(error)
        return None 

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def signin_controller(user):
    try:
        connection =connect()
        cursor = connection.cursor()
        query = 'select * from account where email = %s and password = %s'
        value = (user.email, user.password)
        cursor.execute(query, value)
        result = cursor.fetchall()
        if len(result) != 0:
            return result[0][0] #id 

        else:
            return None 
    
    except connector.Error as error:
        print(error)
        return None 

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def get_list_product():
    try: 
        connection =connect()
        cursor = connection.cursor()
        query = 'select * from product'
        cursor.execute(query) 
        result = cursor.fetchall()
        # print(result)
        return result 

    except connector.Error as error:
        print(error)
        return None 

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def insert_product_to_db(product):
    try:
        connection =connect()
        cursor = connection.cursor()
        query = 'insert into product (name, description, price, quantity, image, id_category) values (%s, %s, %s, %s, %s, %s);'
        value = (product.name, product.description, product.price, product.quantity, product.image, product.id_category)
        cursor.execute(query, value)
        connection.commit()
        return cursor.lastrowid

    except connector.Error as error:
        print(error)
        return None 

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def insert_cart_to_db(cart):
    try:
        connection =connect()
        cursor = connection.cursor()
        query = 'insert into cart (id_account, id_product, amount_product) values (%s, %s, %s);'
        value = (cart.id_account, cart.id_product, cart.amount_product)
        cursor.execute(query, value)
        connection.commit()
        
        return cursor.lastrowid

    except connector.Error as error:
        print(error)
        return None 

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def update_cart_to_db(cart):
    try:
        connection =connect()
        cursor = connection.cursor()
        query = 'update cart set amount_product=%s where id=%s;'
        value = (cart.amount_product, cart.id)
        cursor.execute(query, value)
        connection.commit()

        return cursor.lastrowid

    except connector.Error as error:
        print(error)
        return None 

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            
def update_cart_by_account_product(cart):
    try:
        connection =connect()
        cursor = connection.cursor()
        query = 'select * from cart where id_account=%s and id_product=%s;'
        value = (cart.id_account, cart.id_product)
        cursor.execute(query, value)
        result = cursor.fetchall()
        if len(result) != 0:
            id_cart = result[0][0] #id 
            cart.id = id_cart
            update_success = update_cart_to_db(cart)
            return update_success

        else: # dont have -> insert
            id_cart = insert_cart_to_db(cart)
            return id_cart

    except connector.Error as error:
        print(error)
        return None 

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def get_list_cart_by_id(id_account):
    try:
        connection =connect()
        cursor = connection.cursor()
        query = 'select * from cart, product where cart.id_account=%s and cart.id_product=product.id;'
        value = [id_account]
        cursor.execute(query, value)
        result = cursor.fetchall()
        
        return result

    except connector.Error as error:
        print(error)
        return None 

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

#query bill_product table
def insert_bill_product_to_db(bill_product):
    try:
        connection =connect()
        cursor = connection.cursor()
        query = 'insert into bill_product (id, id_product, amount_product) values (%s, %s, %s);'
        value = (bill_product.id, bill_product.id_product, bill_product.amount_product)
        cursor.execute(query, value)
        connection.commit()
        
        return cursor.lastrowid

    except connector.Error as error:
        print(error)
        return None 

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def update_bill_product_to_db(bill_product):
    try:
        connection =connect()
        cursor = connection.cursor()
        query = 'update bill_product set amount_product=%s where id_product=%s;'
        value = (bill_product.amount_product, bill_product.id)
        cursor.execute(query, value)
        connection.commit()

        return cursor.lastrowid

    except connector.Error as error:
        print(error)
        return None 

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def get_list_bill_product_by_id(id):
    try:
        connection =connect()
        cursor = connection.cursor()
        query = 'select * from bill_product, bill where bill_product.id=%s and bill_product.id=bill.id;'
        value = [id_account]
        cursor.execute(query, value)
        result = cursor.fetchall()
        
        return result

    except connector.Error as error:
        print(error)
        return None 

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

#query bill table
def insert_bill_to_db(bill):
    try:
        connection =connect()
        cursor = connection.cursor()
        query = 'insert into bill (id, id_account, price, discount, phone, address) values (%s, %s, %s, %s, %s, %s);'
        value = (bill.id, bill.id_account, bill.price, bill.discount, bill.phone, bill.address)
        cursor.execute(query, value)
        connection.commit()
        
        return cursor.lastrowid

    except connector.Error as error:
        print(error)
        return None 

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def update_bill_to_db(bill):
    try:
        connection =connect()
        cursor = connection.cursor()
        query = 'update bill set price=%s where id=%s;'
        value = (bill.price, bill.id)
        cursor.execute(query, value)
        connection.commit()

        return cursor.lastrowid

    except connector.Error as error:
        print(error)
        return None 

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def get_list_bill_by_id(id_account):
    try:
        connection =connect()
        cursor = connection.cursor()
        query = 'select * from bill, account where bill.id_account=%s and bill.id_account=account.id_account;'
        value = [id_account]
        cursor.execute(query, value)
        result = cursor.fetchall()
        
        return result

    except connector.Error as error:
        print(error)
        return None 

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

if __name__ == "__main__":
    list_cart = get_list_cart_by_id([1])
    print(list_cart)
#     # sign up
#     # is_sign_up_success = sign_up_user('mail1@gmail.com', "password")
#     # print(is_sign_up_success)

#     # sign in 
#     is_sign_up_success = sign_in_user('mail1@gmail.com', 'password')
#     print(is_sign_up_success)