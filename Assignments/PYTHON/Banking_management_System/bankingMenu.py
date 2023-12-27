from DatabaseConnection import *
from BankingAccount import Account
from bankingSavingAccount import SavingsAccount
from bankingCustomerAccount import CustomerAccount
from BankingTransaction import Transaction
from bankingBank import Bank


class menu(Bank):
    def create_account(self):
        print("Choose the type of account:")
        print("1. Savings Account")
        print("2. Current Account")

        choice = input("Enter your choice (1 or 2): ")

        account_id = input("Enter the account ID: ")
        customer_id = input("Enter the customer ID: ")
        initial_balance = float(input("Enter the initial balance: "))

        if choice == "1":
            interest_rate = float(input("Enter the interest rate for Savings Account: "))
            account = SavingsAccount(get_ids('accounts', 'account_id'), customer_id, initial_balance, interest_rate)
            self.create_customer_account(account)
        elif choice == "2":
            account = CustomerAccount(get_ids('accounts', 'account_id'), customer_id, initial_balance)
            self.create_customer_account(account)
        else:
            print("Invalid choice. Please choose 1 or 2.")
            return

        print("Account created successfully!")
        print("Account details:")

    def menu_details(self):
     bank = menu()
     while True:
        print("\nBank Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Create Account")
        print("4. Calculate Interest")
        print("5. Exit")

        option = input("Enter your option (1-5): ")

        if option == "1":
            account_id = input("Enter the account ID: ")
            amount = float(input("Enter the deposit amount: "))
            bank.deposit(account_id, amount)
        elif option == "2":
            account_id = input("Enter the account ID: ")
            amount = float(input("Enter the withdrawal amount: "))
            bank.withdraw(account_id, amount)
        elif option == "3":
            bank.create_account()
        elif option == "4":
            account_id = input("Enter the account ID: ")
            bank.calculate_interest(account_id)
        elif option == "5":
            print("Exiting the Bank. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option (1-5).")

m = menu()
m.create_account()
