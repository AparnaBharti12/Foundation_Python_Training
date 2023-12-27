import mysql.connector
from mysql.connector import Error


def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aparna@1234",
            port='3306',
            database="ticketbookingsystem"
        )
        return connection
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def get_ids(table_name, id_column_name):
    mydb = create_connection()
    my_cursor = mydb.cursor()
    sql = 'SELECT ' + id_column_name + ' FROM ' + table_name + ' ORDER BY ' + id_column_name + ' DESC LIMIT 1'
    print(sql)
    my_cursor.execute(sql)
    x = list(my_cursor.fetchone())[0]
    return int(x) + 1


