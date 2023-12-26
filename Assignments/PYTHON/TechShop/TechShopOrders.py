from TechShopCustomers import Customers
from datetime import datetime
from DatabaseConnection import create_connection


class Orders:
    def __init__(self, order_id, customer: Customers, order_date, total_amount, order_status="Pending"):
        self.connection = create_connection()
        self.__order_id = order_id
        self.__customer = customer
        self.__order_date = order_date
        self.__total_amount = total_amount
        self.__order_status = order_status

    # Getter for order_id
    def get_order_id(self):
        return self.__order_id

    # Getter for customer
    def get_customer(self):
        return self.__customer

    # Getter for order_date
    def get_order_date(self):
        return self.__order_date

    # Setter for order_date
    def set_order_date(self, order_date):
        cursor = self.connection.cursor()
        sql = 'UPDATE Orders SET OrderDate = %s WHERE OrderID = %s'
        para = (order_date, self.__order_id)
        cursor.execute(sql, para)
        self.__order_date = order_date

    # Getter for total_amount
    def get_total_amount(self):
        return self.__total_amount

    # Setter for total_amount
    def set_total_amount(self, total_amount):
        cursor = self.connection.cursor()
        sql = 'UPDATE Orders SET TotalAmount = %s WHERE OrderID = %s'
        para = (total_amount, self.__order_id)
        cursor.execute(sql, para)
        self.__total_amount = total_amount

    # Getter for order_status
    def get_order_status(self):
        return self.__order_status

    # Setter for order_status
    def set_order_status(self, order_status):
        cursor = self.connection.cursor()
        sql = 'UPDATE Orders SET status= %s WHERE OrderID = %s'
        para = (order_status, self.__order_id)
        cursor.execute(sql, para)
        self.__order_status = order_status

    def calculate_total_amount(self):
        cursor = self.connection.cursor()
        sql = ('SELECT SUM(orderdetails.Quantity*orders.TotalAmount) AS TotalAmount FROM orderdetails JOIN orders on '
               'orderdetails.OrderID = orders.OrderID WHERE orders.OrderID = %s')
        para = (self.__order_id,)
        cursor.execute(sql, para)
        totalamount = list(cursor.fetchone())[0]
        print(totalamount)

    def get_order_details(self):
        cursor = self.connection.cursor()
        q1 = "select * from orders ;"
        cursor.execute(q1)
        val = cursor.fetchall()
        details = f"Order ID: {val[0]}\n"
        details += f"Customer: {val[1]}\n"
        details += f"Order Date: {val[2]}\n"
        details += f"Total Amount: ${val[3]}\n"
        details += f"Order Status: {val[4]}\n"
        print(details)

    def update_order_status(self, new_status):
        cursor = self.connection.cursor()
        sql = 'UPDATE Orders SET status= %s WHERE OrderID = %s'
        para = (new_status, self.__order_id)
        cursor.execute(sql, para)
        self.__order_status = new_status

    def cancel_order(self):
        cursor = self.connection.cursor()
        sql = 'UPDATE Orders SET status= %s WHERE OrderID = %s'
        para = ('Cancelled', self.__order_id)
        cursor.execute(sql, para)
        self.__order_status = "Cancelled"


def orders_object():
    c = Customers(302,"Bob","Johnson","bob@example.com",1551234567,"2","789 Oak St")
    o1 = Orders(302, c, "2023-12-23", 2345, "Shipped")
    return o1
