
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    

    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount} to {self.name}")
        else:
            print("Deposite amount must be not zero")
    
    def get_balance(self):
        return self.__balance
  
acc = BankAccount("Ajay", 1000)
acc.deposite(0)
print(f"current balance is {acc.get_balance()}")  
        
