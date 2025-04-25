
class BankAccount:
  def __init__(self, name, balance):
    self.name = name
    self.__balance = balance


  def deposite(self, amount):
      self.__balance += amount
      print(f"dposite amt is {amount} , name is {self.name}")

  def getBalance(self):
      return self.__balance
    

  # def printAmt(self):
  #   print(f"Your name is {self.name} and amt is {self.__balance}")

# start1 = BankAccount("ajay", "2000")
# start1.printAmt()

strt1 = BankAccount("ajay",200)
strt1.deposite(500)
print(strt1.getBalance())