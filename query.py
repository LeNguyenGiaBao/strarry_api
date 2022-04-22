import mysql.connector as connector

def connect():
    connection = connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="strarry"
    )
    return connection

def sign_up_user_to_db(user):
    try:
        connection =connect()
        cursor = connection.cursor()
        query = 'insert into account (email_account, password_account) values (%s, %s)'
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

def sign_in_user(user):
    try:
        connection =connect()
        cursor = connection.cursor()
        query = 'select * from account where email_account = %s and password_account = %s'
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
        query = 'insert into product (name_product, description_product, price_product, quantity_product, image_product, id_category_product) values (%s, %s, %s, %s, %s, %s);'
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
# if __name__ == "__main__":
#     # sign up
#     # is_sign_up_success = sign_up_user('mail1@gmail.com', "password")
#     # print(is_sign_up_success)

#     # sign in 
#     is_sign_up_success = sign_in_user('mail1@gmail.com', 'password')
#     print(is_sign_up_success)