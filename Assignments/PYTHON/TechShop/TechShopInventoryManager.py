from TechShopInventory import Inventory
from TechShopProducts import Products
from TechShopProductmanager import ProductManager
from DatabaseConnection import create_connection


class InventoryManager:
    def __init__(self):
        self.connection = create_connection()

    def add_to_inventory(self, product_id, quantity=True):
        try:
            quantity_available = 1
            mycursor = self.connection.cursor()
            p1 = ProductManager()
            if quantity == True:
                quantity_available = 1
            else:
                quantity_available = 0
            if p1.product_exists(product_id):
                #  InventoryID | ProductID | QuantityInStock | LastStockUpdate
                sql = "UPDATE Inventory SET QuantityInStock = %s WHERE ProductID = %s"
                value = (quantity_available, product_id)
                mycursor.execute(sql, value)
                self.connection.commit()
            else:
                print(f'Invalid ProductID')
                return

            print(f"Inventory updated successfully. Product ID: {product_id}")
        except Exception as e:
            print(f"Error updating inventory: {e}")

    #
    def remove_from_inventory(self, product_id, quantity=1):
        try:
            mycursor = self.connection.cursor()
            p1 = ProductManager()
            if p1.product_exists(product_id):
                sql = 'UPDATE Inventory SET QuantityInStock = %s WHERE ProductID = %s'
                mycursor.execute(sql,(quantity,product_id))
                self.connection.commit()
            else:
                print(f"Error updating inventory: Product ID {product_id} not found")
        except Exception as e:
            print(f"Error updating inventory: {e}")

    def get_inventory_value(self):
        mycursor = self.connection.cursor()
        sql = '''SELECT SUM(Inventory.QuantityInStock*Products.Price)
                 AS TotalInventoryValue FROM Inventory
                 JOIN Products ON Inventory.ProductID = Products.ProductID'''
        mycursor.execute(sql)
        x = list(mycursor.fetchone())[0]
        return x

    def list_low_stock_products(self, threshold):
        mycursor = self.connection.cursor()
        sql = '''SELECT Products.*, Inventory.QuantityInStock FROM Inventory 
                                JOIN Products ON Inventory.ProductID = Products.ProductID
                                WHERE Inventory.QuantityInStock < %s'''
        para = (threshold,)
        mycursor.execute(sql, para)
        print("All Low Stock Products in Inventory:")
        print("ProductID | ProductName | Description | Price | QuantityInStock \n")
        for item in mycursor.fetchall():
            print(item)

    def list_out_of_stock_products(self):
        mycursor = self.connection.cursor()
        sql = '''SELECT Products.*, Inventory.QuantityInStock FROM Inventory 
                        JOIN Products ON Inventory.ProductID = Products.ProductID
                        WHERE Inventory.QuantityInStock=0'''
        mycursor.execute(sql)
        print("All Out of Stock Products in Inventory:")
        print("ProductID | ProductName | Description | Price | QuantityInStock \n")
        for item in mycursor.fetchall():
            print(item)

    def list_all_products(self):
        mycursor = self.connection.cursor()
        sql = '''SELECT Products.*, Inventory.QuantityInStock FROM Inventory 
                JOIN Products ON Inventory.ProductID = Products.ProductID'''
        mycursor.execute(sql)
        print("All Products in Inventory:")
        print("ProductID | ProductName | Description | Price | QuantityInStock \n")
        for item in mycursor.fetchall():
            print(item)

    def get_product_by_id(self, product_id) -> Products:
        mycursor = self.connection.cursor()
        sql = 'SELECT * FROM Products WHERE ProductID = %s'
        para = (product_id,)
        mycursor.execute(sql, para)
        x = list(mycursor.fetchone())
        return Products(x[0], x[1], x[2], x[3])

# i = InventoryManager()
# i.add_to_inventory(204, 12)
