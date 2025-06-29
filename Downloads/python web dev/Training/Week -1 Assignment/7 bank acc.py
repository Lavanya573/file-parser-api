
class BankAccount:
    def __init__(self, acc_number, acc_holder, balance):
        # Private  variables
        self.__acc_number = acc_number
        self.__acc_holder = acc_holder
        self.__balance = balance

    # Getter
    def get_account_number(self):
        return self.__acc_number

    def get_account_holder(self):
        return self.__acc_holder

    def get_balance(self):
        return self.__balance

    # Setter
    def set_account_number(self, acc_number):
        self.__acc_number = acc_number

    def set_account_holder(self, acc_holder):
        self.__acc_holder = acc_holder

    def set_balance(self, balance):
        self.__balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"\n"
                  f" ₹{amount} deposited successfully!")
        else:
            print(" Enter a valid amount to deposit.")

    # Method to withdraw money with balance check
    def withdraw(self, amount):
        if amount > self.__balance:
            print(" Insufficient balance! Withdrawal failed.")
        elif amount <= 0:
            print(" Enter a valid amount to withdraw.")
        else:
            self.__balance -= amount
            print(f"\n ₹{amount} withdrawn successfully!")

    # Method to display account info
    def display_info(self):
        print("\n--- Account Information ---")
        print("Account Number:", self.__acc_number)
        print("Account Holder:", self.__acc_holder)
        print("Balance: ₹", self.__balance)
try:
    # Input account details
    acc_number = input("Enter Account Number: ")
    acc_holder = input("Enter Account Holder Name: ")
    balance = float(input("Enter Opening Balance: ₹"))

    # Create a BankAccount object
    account = BankAccount(acc_number, acc_holder, balance)

    # Display initial info
    account.display_info()

    # Deposit
    deposit_amt = float(input("\nEnter amount to deposit: ₹"))
    account.deposit(deposit_amt)

    # Withdraw
    withdraw_amt = float(input("\nEnter amount to withdraw: ₹"))
    account.withdraw(withdraw_amt)

    # Display final account info
    account.display_info()

except ValueError:
    print(" Please enter valid numeric values for amounts.")
