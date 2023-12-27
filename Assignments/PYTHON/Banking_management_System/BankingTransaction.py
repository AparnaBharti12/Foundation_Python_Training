from DatabaseConnection import *


class Transaction:

    def __init__(self, transaction_id, account_id, transaction_type, amount, transaction_date):
        self.connection = create_connection()
        self.__transaction_id = transaction_id
        self.__account_id = account_id
        self.__transaction_type = transaction_type
        self.__amount = amount
        self.__transaction_date = transaction_date

    def get_transaction_id(self):
        return self.__transaction_id

    def get_account_id(self):
        return self.__account_id

    def get_transaction_type(self):
        return self.__transaction_type

    def get_transaction_date(self):
        return self.__transaction_date

    def get_transaction_amount(self):
        return self.__amount

    def update_transaction_info(self, transaction_id):

        my_cursor = self.connection.cursor()

        try:

                sql = '''
                       UPDATE Transactions SET account_id = %s,transaction_type = %s
                        ,amount = %s,transaction_date = %s WHERE transaction_id = %s
                     '''
                para = (self.__account_id,self.__transaction_type,self.__amount,self.__transaction_date,transaction_id)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('Transaction date updated successfully')
        except Exception as e:
                print(f'An error occurred: {e}')
        finally:
                self.connection.close()


# t  = Transaction(501,101,"withdrawal",1000,"2023-01-15")
# t.update_transaction_info(501)