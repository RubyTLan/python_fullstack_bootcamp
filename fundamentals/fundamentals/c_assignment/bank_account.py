class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance+=amount
        return self
        # your code here
    def withdraw(self, amount):
        if self.balance<amount:
            self.balance-=5
            print("Insufficient funds:Charging a $5 fee")
            return self
        else:
            self.balance-=amount
            return self
        # your code here
    def display_account_info(self):
        print(f"balance:${self.balance}")
        return self
        # your code here
    def yield_interest(self):
        if self.balance>0:
            self.balance*=(1+self.int_rate)
        return self

account1=BankAccount(0.05,100)
account2=BankAccount(0.05,200)

account1.deposit(100).deposit(100).deposit(100).withdraw(1000).yield_interest().display_account_info()
account2.deposit(200).deposit(200).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info()


# your code here
