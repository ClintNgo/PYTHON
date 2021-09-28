class User:	
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def withdrawal(self,amount):
        self.account_balance -= amount
        if (self.account_balance < 0):
            print (f"{self.name}, your account is insufficient to complete the withdrawal.")
        return self

    def deposit(self,amount):
        self.account_balance += amount
        return self

    def transfer(self,amount,receiver):
        self.account_balance -= amount
        receiver.account_balance += amount
        return self

clint = User("Clint","Clintngo@gmail.com")
kevin = User("Kevin","Kevin@gmail.com")
jack = User("Jack","Jack@gmail.com")

clint.deposit(1000).deposit(500).deposit(2000).withdrawal(100)

kevin.deposit(10000).deposit(2000).withdrawal(3000).withdrawal(3000)

jack.deposit(90000).withdrawal(30100).withdrawal(2000).withdrawal(10000).transfer(10000,clint)


print(f"User:{clint.name}, {clint.email}, Balance: ${clint.account_balance}")
print(f"User:{kevin.name}, {kevin.email}, Balance: ${kevin.account_balance}")
print(f"User:{jack.name}, {jack.email}, Balance: ${jack.account_balance}")


