import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="strarry"
)

cursor = db.cursor()
# account Table
cursor.execute('''
  CREATE TABLE IF NOT EXISTS account (
    id INT NOT NULL AUTO_INCREMENT, 
    email CHAR(50) NOT NULL, 
    password CHAR(50) NOT NULL, 
    name NVARCHAR(50), 
    phone CHAR(50), 
    address NVARCHAR(50), 
    role INT NOT NULL DEFAULT 1, 
    image MEDIUMBLOB, 
    PRIMARY KEY (id)
  );
''')

# category Table
cursor.execute('''
  CREATE TABLE IF NOT EXISTS category (
    id INT NOT NULL AUTO_INCREMENT, 
    name NVARCHAR(50), 
    image MEDIUMBLOB,
    PRIMARY KEY (id)
  );
''')

# product Table
cursor.execute('''
  CREATE TABLE IF NOT EXISTS product (
    id INT NOT NULL AUTO_INCREMENT, 
    name NVARCHAR(50) NOT NULL, 
    description NVARCHAR(256), 
    price INT, 
    quantity INT, 
    image MEDIUMBLOB, 
    id_category INT NOT NULL, 
    PRIMARY KEY (id),
    FOREIGN KEY (id_category) REFERENCES category(id)
  );
''')

# cart Table
cursor.execute('''
  CREATE TABLE IF NOT EXISTS cart (
    id INT NOT NULL AUTO_INCREMENT, 
    id_account INT NOT NULL,
    id_product INT NOT NULL,
    amount_product INT DEFAULT 0,
    PRIMARY KEY (id),
    FOREIGN KEY (id_account) REFERENCES account(id),
    FOREIGN KEY (id_product) REFERENCES product(id)
  );
''')
# Bill Table
cursor.execute('''
  CREATE TABLE IF NOT EXISTS bill (
    id INT NOT NULL AUTO_INCREMENT, 
    id_account INT NOT NULL,
    price INT,
    discount INT,
    phone CHAR(50), 
    address NVARCHAR(50), 
    PRIMARY KEY (id),
    FOREIGN KEY (id_account) REFERENCES account(id)
  );
''')
# Bill_product Table
cursor.execute('''
  CREATE TABLE IF NOT EXISTS bill_product (
    id INT NOT NULL , 
    id_product INT NOT NULL,
    amount_product INT DEFAULT 0,
    FOREIGN KEY (id_product) REFERENCES product(id),
    FOREIGN KEY (id) REFERENCES bill(id)
  );
''')


# INSERT INTO account (email, password) VALUES ('mail1@gmail.com', 'password');
# INSERT INTO category (name) VALUES ('Milk');
# INSERT INTO product (name, id_category) VALUES ('Vinamilk', 1);
# INSERT INTO cart (id_account, id_product, amount_product) VALUES (1, 1, 1);
