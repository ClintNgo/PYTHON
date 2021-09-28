class User:	
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def withdrawal(self,amount):
        self.account_balance -= amount
        if (self.account_balance < 0):
            print (f"{self.name}, your account is insufficient to complete the withdrawal.")

    def deposit(self,amount):
        self.account_balance += amount

    def transfer(self,amount,receiver):
        self.account_balance -= amount
        receiver.account_balance += amount

clint = User("Clint","Clintngo@gmail.com")
kevin = User("Kevin","Kevin@gmail.com")
jack = User("Jack","Jack@gmail.com")

clint.deposit(1000)
clint.deposit(500)
clint.deposit(2000)
clint.withdrawal(100)
kevin.deposit(10000)
kevin.deposit(2000)
kevin.withdrawal(3000)
kevin.withdrawal(3000)
jack.deposit(90000)
jack.withdrawal(30100)
jack.withdrawal(2000)
jack.withdrawal(10000)
jack.transfer(10000,clint)

print(f"User:{clint.name}, {clint.email}, Balance: ${clint.account_balance}")
print(f"User:{kevin.name}, {kevin.email}, Balance: ${kevin.account_balance}")
print(f"User:{jack.name}, {jack.email}, Balance: ${jack.account_balance}")


