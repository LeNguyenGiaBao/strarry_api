import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="baole",
  password="12345678"
)

print(mydb)