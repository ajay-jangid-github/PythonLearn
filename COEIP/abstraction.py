
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
  @abstractmethod
  def process_payment(self, amount):
    pass


class Razorpay(PaymentGateway):
  def process_payment(self, amount):
    print(f"{amount} processed by Razorpay")

class Paypal(PaymentGateway):
  def process_payment(self, amount):
    print(f"{amount} processed by Paypal")

class Googlepay(PaymentGateway):
  def process_payment(self, amount):
    print(f"{amount} Processed by googlepay")
  
def checkout(gateway: PaymentGateway, amount):
  gateway.process_payment(amount)

checkout(Razorpay(), 1000)
checkout(Paypal(), 2000)
checkout(Googlepay(), 3000)