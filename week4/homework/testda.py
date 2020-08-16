import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Natthapol",
  password="10042541"
)

print(mydb)