#Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Balance: ${self.balance}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. Balance: ${self.balance}")
            else:
                print("Insufficient funds")
        else:
            print("Withdrawal amount must be greater than 0")

account = Account("KBTU", 100)

account.deposit(50)
account.withdraw(30)
account.withdraw(200)
account.deposit(-20)

#Deposited $50. Balance: $150
#Withdrew $30. Balance: $120
#Insufficient funds
#Deposit amount must be greater than 0.