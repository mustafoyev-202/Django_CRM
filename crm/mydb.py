import mysql.connector

database = mysql.connector.connect(
    host="",
    user="",
    password="",
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE baxtiyor")
print("Database created successfully")
