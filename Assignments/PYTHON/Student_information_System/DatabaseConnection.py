import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aparna@1234",
            port='3306',
            database="sisdb"
        )
        return connection
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None

