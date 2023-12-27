from DatabaseConnection import *
from BankingAccount import Account


class ZeroBalanceAccount(Account):

    def __init__(self, account_id, customer_id, account_type):
        self.connection = create_connection()
        super().__init__(account_id, customer_id, account_type, 0)