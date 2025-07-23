class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private - cannot be modified directly

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)    # Works: balance = 1500
account.withdraw(200)   # Works: balance = 1300
account.withdraw(2000)  # Blocked: "Insufficient funds" msg