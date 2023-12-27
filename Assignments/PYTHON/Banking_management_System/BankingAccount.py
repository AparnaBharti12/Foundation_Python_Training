from DatabaseConnection import *


class Account:

    def __init__(self, account_id, customer_id, account_type, balance):
        self.customer_id = customer_id
        self.connection = create_connection()
        self.__account_id = account_id
        self.__customer_id = customer_id
        self.__account_type = account_type
        self.__balance = balance

    def get_account_id(self):
        return self.__account_id

    def get_customer_id(self):
        return self.__customer_id

    def get_account_type(self):
        return self.__account_type

    def get_balance(self):
        return self.__balance

    def update_account_details(self):
        my_cursor = self.connection.cursor()
        try:
            sql = '''
            UPDATE Accounts SET customer_id  = %s,account_type = %s,balance=%s WHERE account_id = %s
            '''
            para = (self.customer_id,self.__account_type,self.__balance,self.__account_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Account Type updated successfully')
        except Exception as e:
            print(f"Exception details  : {e}")
        finally:
            self.connection.close()

    def deposit(self, amount,account_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                     UPDATE Accounts SET balance = balance+%s WHERE account_id = %s
                    '''
            para = (amount,account_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Amount deposited successfully')
        except Exception as e:
            print(f'An error occurred: {e}')

    def withdraw(self, amount,account_id):

        my_cursor = self.connection.cursor()
        my_cursor.execute("select balance from accounts where account_id   = %s",(account_id,))
        val = my_cursor.fetchone()
        if amount > val[0]:
            print('Insufficient balance')
            return
        try:
            sql = '''
                     UPDATE Accounts SET balance = balance-%s WHERE account_id = %s
                    '''
            para = (amount,account_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Amount withdrawn successfully')
        except Exception as e:
            print(f'An error occurred: {e}')

    def calculate_interest(self):
        print(f'Amount after interest: ${self.__balance + (self.__balance * 0.45)}')
        return self.__balance + (self.__balance * 0.45)

    def print_account_info(self):
        print('Account ID:', self.__account_id)
        print('Account Type:', self.__account_type)
        print('Account Balance:', self.__balance)

# a   =Account(110,3,"savings",200)
# a.update_account_details()
# a.deposit(3000,101)
# a.withdraw(30,101)