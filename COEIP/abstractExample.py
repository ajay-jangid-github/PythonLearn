# this is module abc, and ABC makes your class abstract, and abstratmethod -must be implemented in child classes
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
  @abstractmethod
  def payment_processing(self, amount):
    pass

class Razorpay(PaymentGateway):
  def payment_processing(self, amount):
    print(f"{amount} processd by razorpay")

class Paypal(PaymentGateway):
  def payment_processing(self, amount):
    print(f"{amount} processed by Paypal")

class GooglePay(PaymentGateway):
  def payment_processing(self, amount):
    print(f"{amount} processed by Googlepay")

def checkout(gateway: PaymentGateway, amount):
    gateway.payment_processing(amount)


checkout(Razorpay(), 2000)
checkout(Paypal(),3000) 
checkout(GooglePay(), 4000)
  # checkout(GooglePay(), 4000)



