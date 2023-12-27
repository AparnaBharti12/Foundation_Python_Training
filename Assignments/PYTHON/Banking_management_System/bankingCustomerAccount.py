from DatabaseConnection import *
from BankingAccount import Account


class CustomerAccount(Account):
    OVERDRAFT_LIMIT = 1000

    def __init__(self, account_id, customer_id, balance):
        super().__init__(account_id, customer_id, account_type="Current", balance=balance)
        self.__overdraft_limit = self.OVERDRAFT_LIMIT

    def withdraw(self, amount,account_id):
        my_cursor = self.connection.cursor()
        my_cursor.execute("select balance from accounts where account_id   = %s", (account_id,))
        val = my_cursor.fetchone()
        if amount > val[0]:
            print('Insufficient balance')
            return

        try:
            my_cursor = super().connection.cursor()
            sql = '''
                UPDATE Accounts SET balance = balance-%s WHERE account_id = %s
            '''
            para = (val[0]-amount,account_id)
            my_cursor.execute(sql, para)
            super().connection.commit()
        except Exception as e:
            print(f'An error occurred: {e}')