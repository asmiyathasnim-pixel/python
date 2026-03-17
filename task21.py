# 1⃣ Bank Account Class 
# Create a BankAccount class: 
# ● Keep balance private. 
# ● Add deposit(amount) and withdraw(amount) methods. 
# ● Prevent withdrawal if amount > balance. 
# ● Store transactions and show last 5. 
# Methods / Concepts to Use: 
# ● Constructor __init__ 
# ● Instance methods 
# ● Encapsulation (private variable) 
# ● List handling 

class Bank:
    def __init__(self, balance=0):
        self.__balance = balance
        self.__transaction = []

    def deposit(self, amount):
        if amount > 0 :
            self.__balance += amount
            self.__transaction.append(f"Deposite $ : {amount}")
            print(f"${amount} deposited successfully")

        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not Enough Balance")

        elif amount <= 0:
            print("Invalid amount")

        else:
            self.__balance -= amount
            self.__transaction.append(f"Withdrawn $ : {amount}")
            print(f"${amount} Withdrawn Successfully")

    def show_balance(self):
        print("Current Balance : ", self.__balance)

    def last_5(self):
        print("Last 5 Transactions : ")
        for i in self.__transaction[-5 :]:
            print(i)

account = Bank(100)

account.deposit(100)
account.withdraw(50)
account.deposit(200)
account.withdraw(500)
account.deposit(100)
account.withdraw(20)

account.show_balance()
account.last_5()