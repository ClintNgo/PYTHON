class BankAccount:
    bank_name = "Bank of Dojo for Ninjas"
    accounts = []
    def __init__(self, name, int_rate,balance):
        self.name = name
        self.int_rate = int_rate
        self.account_balance = balance
        BankAccount.accounts.append(self)

    def withdrawal(self,amount):
        self.account_balance -= amount
        if (self.account_balance < 0):
            print (f"Insufficient funds: Charging a $5 fee")
            self.account_balance - 5
        return self

    def deposit(self,amount):
        self.account_balance += amount
        return self

    def display_account_info(self):
        print(self.account_balance)
        return self

    def yield_interest(self):
        self.account_balance *= self.int_rate
        return self

    @classmethod
    def all_accounts(cls):
        print("Accounts:")
        for account in BankAccount.accounts:
            print (f"Account: {account.name} | Interest Rates: {account.int_rate} | Account Balance: ${account.account_balance}")

class User:
    def __init__(self,name):
        self.name = name
        self.account = BankAccount(int_rate=0.03,balance=0)
        return self

    def make_deposit(self, amount,account):
        self.account.deposit(0)
        print(self.account.account_balance)
        return self

    def make_withdrawal(self, amount, account ):
        self.account.withdrawal(0)
        print(self.account.account_balance)
        return self

    def display_account_info(self):
        print(self.account.account_balance)
        return self




clint = BankAccount("Clint - checking", .05, 10000)
kevin = BankAccount("Kevin", .035,30000)

clint.deposit(1000)
clint.deposit(1000).deposit(500).deposit(2000).withdrawal(100).yield_interest().display_account_info()
kevin.deposit(10000).deposit(2000).withdrawal(3000).withdrawal(3000).withdrawal(1000).withdrawal(1000).yield_interest().display_account_info()

BankAccount.all_accounts()