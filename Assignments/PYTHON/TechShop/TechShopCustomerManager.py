from TechShopCustomers import Customers
from DatabaseConnection import create_connection
import re


class CustomerManager:
    def __init__(self):
        self.connection = create_connection()

    def register_customer(self, customer_id,first_name, last_name, email, phone,address):
        try:
            # Validating input data
            self.validate_customer_data(email)
            # Checking if the email already exists in the database
            if self.is_email_duplicate(email):
                raise ValueError("Email address is already registered.")

            cursor = self.connection.cursor()

            #  CustomerID | FirstName | LastName | Email               | Phone      | Address
            sql2 = 'INSERT INTO Customers(CustomerID, FirstName, LastName, Email,phone,address) VALUES(%s, %s, %s,%s, %s, %s)'
            para = (customer_id, first_name, last_name, email,phone, address)
            cursor.execute(sql2, para)
            self.connection.commit()
            self.connection.close()
            print("Customer registration successful.")
        except Exception as e:
            print(f"Error registering customer: {e}")

    def validate_customer_data(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not re.fullmatch(regex, email):
            raise ValueError("Invalid email address.")

    def is_email_duplicate(self, email):
        cursor = self.connection.cursor()
        sql = 'SELECT * FROM Customers WHERE email = %s'
        para = (email,)
        cursor.execute(sql, para)
        x = len(list(cursor.fetchall()))
        if (x > 0):
            return True
        return False


