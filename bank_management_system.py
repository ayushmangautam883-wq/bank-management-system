import os

FILE_NAME = "accounts.txt"


class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance}")


class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.load_accounts()

    def create_account(self):
        name = input("Enter account holder name: ")
        account_number = input("Enter account number: ")

        if account_number in self.accounts:
            print("Account already exists.")
            return

        account = BankAccount(name, account_number)
        self.accounts[account_number] = account
        self.save_accounts()

        print("Account created successfully.")

    def deposit_money(self):
        account_number = input("Enter account number: ")

        if account_number in self.accounts:
            amount = float(input("Enter amount to deposit: ₹"))
            self.accounts[account_number].deposit(amount)
            self.save_accounts()
        else:
            print("Account not found.")

    def withdraw_money(self):
        account_number = input("Enter account number: ")

        if account_number in self.accounts:
            amount = float(input("Enter amount to withdraw: ₹"))
            self.accounts[account_number].withdraw(amount)
            self.save_accounts()
        else:
            print("Account not found.")

    def check_balance(self):
        account_number = input("Enter account number: ")

        if account_number in self.accounts:
            self.accounts[account_number].display_balance()
        else:
            print("Account not found.")

    def save_accounts(self):
        with open(FILE_NAME, "w") as file:
            for acc in self.accounts.values():
                file.write(f"{acc.name},{acc.account_number},{acc.balance}\n")

    def load_accounts(self):
        if not os.path.exists(FILE_NAME):
            return

        with open(FILE_NAME, "r") as file:
            for line in file:
                name, account_number, balance = line.strip().split(",")
                self.accounts[account_number] = BankAccount(
                    name, account_number, float(balance)
                )

    def menu(self):
        while True:
            print("\n===== BANK MANAGEMENT SYSTEM =====")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.deposit_money()
            elif choice == "3":
                self.withdraw_money()
            elif choice == "4":
                self.check_balance()
            elif choice == "5":
                print("Thank you for using the Bank Management System.")
                break
            else:
                print("Invalid choice. Please try again.")


bank = BankSystem()
bank.menu()