class Vehicale:
  def __init__(self, vehicaleName):
    self.vehicalName = vehicaleName

  def show_vehicale(self):
    print(f"Your VehicaleName: {self.vehicalName}")

  def book(self):
    print(f"Your Vehicale is booked")

# sub class 
class Car(Vehicale):
  def __init__(self, vehicaleName, carType):
    super().__init__(vehicaleName)
    self.carType = carType

  def list_car(self):
    print(f"Your car is added {self.carType}")

  def book(self):
    print(f"your car is booked {self.carType}")


class Bike(Vehicale):
  def __init__(self, vehicalName, bikeType):
    super().__init__(vehicalName)
    self.bikeType = bikeType

  def list_bike(self):
    print(f"Your bike is listed: {self.bikeType}")

  def book(self):
    print(f"Your bike is booked: {self.bikeType}")


# create Object
car1 = Car("Hyundi","Sedan")
Bike1 = Bike("Honda","Super Bike")

# call method

car1.show_vehicale()
car1.list_car()
car1.book()

Bike1.show_vehicale()
Bike1.list_bike()
Bike1.book()