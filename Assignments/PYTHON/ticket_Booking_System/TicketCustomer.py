from DatabaseConnection import *


class Customer:
    def __init__(self, customer_id, customer_name, email, phone_number, booking_id):
        self.connection = create_connection()
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.email = email
        self.phone_number = phone_number
        self.booking_id = booking_id

    # Getter and setter methods
    def get_customer_id(self):
        return self.customer_id

    def get_customer_name(self):
        return self.customer_name

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    def get_booking_id(self):
        return self.booking_id

    def update_customer_info(self, customer_name, email, phone_number, booking_id):
        connection = create_connection()
        cur = connection.cursor(buffered=True)
        q1 = """
        update customer set customer_id = %s,customer_name = %s,email = %s,phone_number = %s,booking_id = %s
        """
        q2 = (customer_name, email, phone_number, booking_id)
        cur.execute(q1, q2)
        print('Customer details updated successfully')

    def display_customer_details(self,customer_id):
        connection = create_connection()
        cur = connection.cursor(buffered=True)
        cur.execute("select * from customer where customer_id  = %s",(customer_id,))
        val = cur.fetchall()
        for i in val:
            print(f"\n\nCUSTOMER ID  : {i[0]}")
            print(f"CUSTOMER NAME  : {i[1]}")
            print(f"EMAIL  : {i[2]}")
            print(f"PHONE NUMBER  : {i[3]}")
            print(f"BOOKING ID  : {i[4]}")
