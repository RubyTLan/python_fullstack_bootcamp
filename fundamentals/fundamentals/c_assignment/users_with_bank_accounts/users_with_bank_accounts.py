class BankAccount:

    def __init__(self,int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance

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

class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.account_dic={"default":BankAccount(int_rate=0.05,balance=0)}

    def create_account(self,account_key):
        self.account_dic[account_key]=BankAccount(int_rate=0.05,balance=0)

    def make_deposit(self,amount,account_key):
        self.account_dic[account_key].balance+=amount

    def make_withdrawal(self,amount,account_key):
        if self.account_dic[account_key].balance<amount:
            self.account_dic[account_key].balance-=5
            print("Insufficient balance!")
        else:
            self.account_dic[account_key].balance-=amount

    def display_user_balance(self,account_key):
        print(self.account_dic[account_key].balance)

    def transfer_money(self,amount,account_key,other_user):
        if self.account_dic[account_key].balance<amount:
            print("Transfer failed!")
        else:
            self.account_dic[account_key].balance-=amount
            other_user.account_dic["default"].balance+=amount



user1=User("Tian","l@gmail.com")
user2=User("Xiao","x@gmail.com")

user1.make_deposit(100,"default")
user1.transfer_money(50,"default",user2)

print(user1.account_dic["default"].balance)
print(user2.account_dic["default"].balance)
