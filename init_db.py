import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="strarry"
)

cursor = db.cursor()
cursor.execute('''CREATE TABLE account (
                id INT NOT NULL AUTO_INCREMENT, 
                email_account CHAR(50) NOT NULL, 
                password_account CHAR(50) NOT NULL, 
                name_account NVARCHAR(50) NULL, 
                phone_account CHAR(50) NULL, 
                address_account NVARCHAR(50) NULL, 
                role_account INT NOT NULL, 
                image_account MEDIUMBLOB NULL, 
                PRIMARY KEY (id));''')