from TechShopProducts import Products, product_object
from TechShopInventory import Inventory
from TechShopCustomers import Customers, Customer_obj
from TechShopOrders import Orders, orders_object
from TechShopOrderDetails import OrderDetails
from TechShopProductmanager import ProductManager
from TechShopCustomerManager import CustomerManager
from TechShopInventoryManager import InventoryManager
from TechShopOrderManager import OrderManager

print("WELCOME TO THE MENU FOR ADMIN ")
print("PRESS NUMBERS 1 TO 5")
print("PRESS 1 TO REGISTER A NEW CUSTOMER")
print("PRESS 2 TO DISPLAY CUSTOMER DETAILS ")
print("PRESS 3 TO CALCULATE TOTAL  ORDERS ")
print("PRESS 4 TO UPDATE CUSTOMER DETAILS ")
print("PRESS 5 TO DISPLAY PRODUCTS ")
print("PRESS 6 TO UPDATE PRODUCTS PRICE ")
print("PRESS 7 TO DISPLAY ORDER DETAILS ")
print("PRESS 8 TO UPDATE ORDER STATUS ")
print("PRESS 9 TO CANCEL  ORDER ")
print("PRESS 10 TO UPDATE ORDER STATUS")
print("PRESS 11 TO  ADD TO INVENTORY")
print("PRESS 12 TO REMOVE FROM INVENTORY")
print("PRESS 13 TO DISPLAY LOW STOCK  PRODUCTS")
ch = int(input("ENTER YOUR CHOICE HERE "))
if ch == 1:
    # first_name, last_name, email, phone, num_orders, address
    Customer_id = input("ENTER CUSTOMER ID  : ")
    first_name = input("ENTER FIRST NAME  : ")
    last_name = input("ENTER LAST NAME  : ")
    email = input("ENTER EMAIL  : ")
    phone = int(input("ENTER PHONE NUMBER   : "))
    address = input("ENTER ADDRESS  : ")
    cm = CustomerManager()
    cm.register_customer(Customer_id, first_name, last_name, email, phone, address)

if ch == 2:
    Customers.get_customer_details()
if ch == 3:
    c1 = Customer_obj()
    c1.calculate_total_orders()
if ch == 4:
    val = input("ENTER DETAILES TO BE UPDATED  : ")
    c1 = Customer_obj()
    c1.update_customer_info(val)
if ch == 5:
    p1 = product_object()
    p1.get_product_details()
if ch == 6:
    p1 = product_object()
    val = int(input("ENTER PRICE TO  UPDATE IN The RECORD  : "))
    p1.update_product_info(val)
if ch == 7:
    o1 = orders_object()
    o1.get_order_details()
if ch == 8:
    o1 = orders_object()
    o1.update_order_status()
if ch == 9:
    o1 = orders_object()
    o1.cancel_order()
if ch == 10:
    order_id = int(input("ENTER  ORDER ID : "))
    status = input("ENTER ORDER STATUS : ")
    # update_order_status(self, order_id, new_status):
    o = OrderManager()
    o.update_order_status(order_id, status)
if ch == 11:
    i = InventoryManager()
    product_id = input("ENTER PRODUCT ID : ")
    quantity = bool(input("ENTER QUANTITY : "))
    i.add_to_inventory(product_id, quantity)
if ch == 12:
    i = InventoryManager()
    product_id = int(input("ENTER PRODUCT ID : "))
    quantity = bool(input("IS PRODUCT IN STOCK TRUE/FALSE : "))
    i.remove_from_inventory(product_id, quantity)
if ch == 13:
    i = InventoryManager()
    i.list_out_of_stock_products()
