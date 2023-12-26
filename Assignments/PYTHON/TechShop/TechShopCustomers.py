from DatabaseConnection import create_connection
from datetime import datetime


class Customers:
    def __init__(self, customer_id, first_name, last_name, email,phone, num_orders, address):
        self.connection = create_connection()
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__num_orders = num_orders
        self.__address = address

    def calculate_total_orders(self):
        cursor = self.connection.cursor()
        sql = 'select %s, Count(*) AS No_Of_Orders from orders where CustomerID = %s;'
        para = (self.__customer_id, self.__customer_id)
        cursor.execute(sql, para)
        temp = list(cursor.fetchone())
        return temp[1]

    @staticmethod
    def get_customer_details():
        connection = create_connection()
        cursor = connection.cursor(buffered=True)
        q1 = "select * from customers ;"
        cursor.execute(q1)
        val = cursor.fetchall()
        details = f"Customer ID: {val[0]}\n"
        details += f"Name: {val[1]} {val[2]}\n"
        details += f"Email: {val[3]}\n"
        details += f"Phone: {val[4]}\n"
        details += f"Address: {val[5]}\n"
        print(f" \n\n{details}")

    def update_customer_info(self, email=None, phone=None, address=None):
        if email:
            cursor = self.connection.cursor()
            sql = 'UPDATE Customers SET email = %s WHERE CustomerID = %s'
            para = (email, self.__customer_id)
            cursor.execute(sql, para)
            self.connection.commit()
            self.__email = email
        if phone:
            cursor = self.connection.cursor()
            sql = 'UPDATE customers SET phone = %s WHERE customer_id = %s'
            para = (phone, self.__customer_id)
            cursor.execute(sql, para)
            self.__phone = phone
            self.connection.commit()
        if address:
            cursor = self.connection.cursor()
            sql = 'UPDATE customers SET address = %s WHERE customer_id = %s'
            para = (address, self.__customer_id)
            cursor.execute(sql, para)
            self.__address = address
            self.connection.commit()

    def get_num_orders(self):
        return self.__num_orders

    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address


def Customer_obj():
    c1 = Customers(1, "john", "Doe", "Doe@example.com ",3454554,4, "121 Down street")
    return c1
