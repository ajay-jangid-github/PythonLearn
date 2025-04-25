# Encapsulation -- means to hide sensititve data from thr user
#  in python to hide data
# 1. private member = __variabe_name
# 2. protected member = _variable_name
# 3. public member = variable_name


class BankAccount:
  def __init__(self, name, balance):
    self.name = name # public member
    self.__balance = balance # protected member
  
  def deposite(self, amount):
    self.__balance += amount
    print(f"deposited {amount} to {self.name} account")

  def get_balance(self):
    return self.__balance

acc = BankAccount("Ajay", 1000)
acc.deposite(500)
print(f"current balance of {acc.get_balance()}")