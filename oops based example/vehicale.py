# Vehicle → base class

# Car, Bike → subclasses

# Method: book() should behave differently for each

class Vehicle:
  def __init__(self, vehicalname):
    self.vehicalname = vehicalname

  
  def show_vehicle(self):
    print(f"vehicalname : {self.vehicalname}")

  def book(self):
    print("Booking a  vehicale")

# sub class
class Car(Vehicle):
  def __init__(self, vehicalname, cartype):
    super().__init__(vehicalname)
    self.cartype = cartype

  
  def list_car(self):
    print(f"added a car {self.cartype}")

  def book(self):
    print(f"booking a car :{self.cartype}")

    # sub class
class Bike(Vehicle):
  def __init__(self, vehicalname, biketype):
    super().__init__(vehicalname)
    self.biketype = biketype

  
  def list_bike(self):
    print(f"added a bike {self.biketype}")

  def book(self):
    print(f"booking a bike :{self.biketype}")

# objects
car1 = Car("hyundi car","sedan")
bik1 = Bike("honda", "superbike")

# Method  calls
car1.show_vehicle()
car1.list_car()
car1.book()


bik1.show_vehicle()
bik1.list_bike()
bik1.book()

  

  
