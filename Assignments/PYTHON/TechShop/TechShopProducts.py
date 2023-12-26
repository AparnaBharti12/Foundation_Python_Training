from DatabaseConnection import create_connection
from datetime import datetime


class Products:
    def __init__(self, product_id, product_name, description, price):
        self.connection = create_connection()
        self.__product_id = product_id
        self.__product_name = product_name
        self.__description = description
        self.__price = price

    def get_product_id(self):
        return self.__product_id

    def set_product_id(self, product_id):
        sql = 'UPDATE Products SET productID = %s WHERE productID = %s'
        para = (product_id, self.__product_id)
        cursor = self.connection.cursor()
        cursor.execute(sql, para)
        self.__product_id = product_id

    def get_product_name(self):
        return self.__product_name

    def set_product_name(self, product_name):
        sql = 'UPDATE Products SET productName = %s WHERE productID = %s'
        para = (product_name, self.__product_id)
        cursor = self.connection.cursor()
        cursor.execute(sql, para)
        self.__product_name = product_name

    def get_description(self):
        return self.__description

    def set_description(self, description):
        sql = 'UPDATE Products SET description = %s WHERE productID = %s'
        para = (description, self.__product_id)
        cursor = self.connection.cursor()
        cursor.execute(sql, para)
        self.__description = description

    def get_price(self):
        return self.__price

    def set_price(self, price):
        sql = 'UPDATE Products SET price = %s WHERE productID = %s'
        para = (price, self.__product_id)
        cursor = self.connection.cursor()
        cursor.execute(sql, para)
        self.__price = price

    def get_product_details(self):
        cursor = self.connection.cursor()
        q1 = "select * from products ;"
        cursor.execute(q1)
        val = cursor.fetchall()
        details = f"Product ID: {val[0]}\n"
        details += f"Product Name: {val[1]}\n"
        details += f"Description: {val[2]}\n"
        details += f"Price: ${val[3]}\n"
        print(details)

    def update_product_info(self, price=None, description=None):
        if price:
            cursor = self.connection.cursor()
            sql = 'UPDATE Products SET price = %s WHERE productID = %s'
            para = (price, self.__product_id)
            cursor.execute(sql, para)
            self.__price = price
            self.connection.commit()
        if description:
            cursor = self.connection.cursor()
            sql = 'UPDATE Products SET description = %s WHERE productID = %s'
            para = (description, self.__product_id)
            cursor.execute(sql, para)
            self.__description = description
            self.connection.commit()

    def is_product_in_stock(self):
        cursor = self.connection.cursor()
        sql = ('SELECT inventory.QuantityInStock FROM products JOIN inventory ON products.ProductID = '
               'inventory.ProductID WHERE products.ProductID = %s')
        para = (self.__product_id,)
        cursor.execute(sql, para)
        x = list(cursor.fetchone())[0]
        return x > 0


def product_object():
    p1 = Products(204, "Microwave Oven",
                  "Effortlessly prepare meals with our versatile microwave oven. It offers quick and convenient cooking options","3000")
    return p1
