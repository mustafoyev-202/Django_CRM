import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="19032006",
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE baxtiyor")
print("Database created successfully")