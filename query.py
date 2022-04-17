import mysql.connector as connector

db = connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="strarry"
)

cursor = db.cursor()

def sign_up_user(user):
    try:
        query = 'insert into account (email_account, password_account, role_account) values (%s, %s, %s)'
        value = (user.email, user.password, user.role_account)

        cursor.execute(query, value)
        db.commit()
        return cursor.lastrowid
    
    except connector.Error as error:
        print(error)
        return None 

def sign_in_user(user):
    try:
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


# if __name__ == "__main__":
#     # sign up
#     # is_sign_up_success = sign_up_user('mail1@gmail.com', "password")
#     # print(is_sign_up_success)

#     # sign in 
#     is_sign_up_success = sign_in_user('mail1@gmail.com', 'password')
#     print(is_sign_up_success)