from DatabaseConnection import *


class Customer:

    def __init__(self, customer_id, first_name, last_name, dob, email, phone_number, address):
        self.connection = create_connection()
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__dob = dob
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address

    def get_customer_id(self):
        return self.__customer_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_customer_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def get_customer_address(self):
        return self.__address

    def update_customer_info(self):
        my_cursor = self.connection.cursor()
        try:
            sql = '''
                UPDATE Customers SET first_name = %s,last_name =%s,DOB  = %s,email = %s,
                phone_number  = %s,address = %s WHERE customer_id = %s
            '''
            para = (self.__first_name, self.__last_name, self.__dob, self.__email, self.__phone_number, self.__address,
                    self.__customer_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
        except Exception as e:
            print(f"Exception details {e}")

        print('Customer Details Updated Successfully')


# c = Customer(2, "Bob", "Johnson", "1988-04-10", "bob@example.com", 9876543210, "5678 Oak Avenue")
# c.update_customer_info()
