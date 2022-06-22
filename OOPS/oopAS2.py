class BankAccount:
    intrest_rate = 0.05
    def __init__(self,name,balance=0) -> None:
        self.name = name
        self.balance = balance
        self.transactions = []
        #self.transactions.append(f"*****Inital deposit : {balance}*****")

    def deposit(self, amount):
        self.balance = self.balance + amount
        #self.transactions.append(f"Amount deposit: {amount}")

    def withdraw(self,amount):
        if amount > self.balance:
            raise Exception("Insufficent Funds")
        self.balance = self.balance - amount
        self.transactions.append(f"Amount withdraw: {amount}")

    def statement(self):
        for item in self.transactions:
            print(item)
        print(f"******** Total Balance {self.balance} ******")

    def transfer_funds(self, to_account, amount):
        if amount > self.balance:
            raise Exception("Insufficent Funds!!")
        to_account.deposit(amount)
        self.balance -= amount
    
    def roi(self):
        intrest_amount = self.balance* BankAccount.intrest_rate
        self.balance = self.balance + intrest_amount


c1 = BankAccount("Steve",1000)
c2 = BankAccount("Bill",2000)
c3 = BankAccount("Alen",3000)
c4 = BankAccount("Alex")

#Before Deposit()

#print(c1.__dict__)
#print(c2.__dict__)
#print(c3.__dict__)
#print(c4.__dict__)

# After Deposit

BankAccount.deposit(c1,1000)  #OR
#c1.deposit(c1, 1000)
#print(c1.__dict__)
c2.deposit(500)
#print(c2.__dict__)
c3.deposit(1000)
#print(c3.__dict__)
c4.deposit(1000)
#print(c4.__dict__)

#After withdraw()
c3.withdraw(1000)
print(c3.balance)
print(c3.__dict__)

c1.deposit(250)
print(c1.__dict__)
#c1.transactions(50)
#print(c1.__dict__)
#c1.balance
#print(c1.__dict__)
c1.deposit(175)
c1.deposit(45)
c1.withdraw(123)
c1.statement()

c3.balance
print(c3.__dict__)
print(c4.__dict__)
c3.transfer_funds(c4,100)
c3.balance
print(c3.__dict__)
print(c4.__dict__)

print (c1.roi())
print(c2.roi())