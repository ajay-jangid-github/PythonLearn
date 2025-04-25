

class BankAccount:
  def __init__(self, name, balance):
    self.name = name
    self.__balance = balance
  
  def deposite(self, amount):
    self.__balance += amount
    print(f"Deposited {amount} to {self.name}")


  def get_balance(self):
    return self.__balance
  
acc = BankAccount("Ajay",1000)
acc.deposite(500)
print(f"Balance  is {acc.get_balance()}")