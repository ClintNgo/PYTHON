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
            print (f"Account: {account.name} | Account Balance: ${account.account_balance}")


clint = BankAccount("Clint", 5, 10000)
kevin = BankAccount("Kevin", 3.5,30000)

clint.deposit(1000).deposit(500).deposit(2000).withdrawal(100).yield_interest().display_account_info()
kevin.deposit(10000).deposit(2000).withdrawal(3000).withdrawal(3000).withdrawal(1000).withdrawal(1000).yield_interest().display_account_info()

BankAccount.all_accounts()