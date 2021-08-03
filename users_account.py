class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        
    def deposit(self, amount):
        self.balance+=amount
        return self
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds charging a $5 fee")
            self.balance -= 5
        return self    
        
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
        
    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self
    
    @classmethod
    def all_instances(cls):
        for account in cls.all_accounts:
            account.display_account_info()


# harini = BankAccount(0.01,0)
# pk = BankAccount(0.02,0)

# harini.deposit(200).deposit(300).deposit(400).withdraw(300).yield_interest().display_account_info()
# pk.deposit(200).deposit(1300).withdraw(50).withdraw(10).withdraw(300).withdraw(100).yield_interest().display_account_info()
# print("=" * 80)
# BankAccount.all_instances()


class User:

    def __init__(self,name,email,account_number):
        self.name = name
        self.email = email
        self.account_number = account_number
        self.account = BankAccount(int_rate=0.02,balance=0)
        # self.savings_account = BankAccount(int_rate=0.02,balance=0)

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self
    # def make_savings_withdrawal(self,amount):
    #     self.savings_account.withdraw(amount)
    #     return self


    def make_deposits(self,amount):
        self.account.deposit(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

    # def transfer_money(self,amount,user):
    #     self.amount -= amount 
    #     user.amount += amount
    #     self.display_user_balance()
    #     user.display_user_balance()
    #     return self

harini = User("Harini","har@cd.com",1234)
harini_checking = User("Harini","har@cd.com",2468)
micheal = User("Micheal","mic@cd.com",2345)
sheldon = User("Sheldon","shel@cd.com",5689)

# 3 deposits and 1 withdrawal and then display their balance
harini.make_deposits(100) 
harini.display_user_balance()
# .make_deposits(400).make_deposits(800).make_withdrawal(800).display_user_balance()

# make 2 deposits and 2 withdrawals
# micheal.make_deposits(1400).make_deposits(1000).make_withdrawal(800).make_withdrawal(800).display_user_balance()

# # 1 deposits and 3 withdrawals 
# sheldon.make_deposits(1400).make_withdrawal(800).make_withdrawal(100).make_withdrawal(100).display_user_balance()

# Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
# harini.transfer_money(300,sheldon)