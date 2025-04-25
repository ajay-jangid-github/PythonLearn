
class vehicle:
  def __init__(self, vehicalName):
    self.vehicalName = vehicalName

  def vehical_Show(self):
    print(f"Vehicale is: {self.vehicalName}")

  def park_vehicle(self):
    print(f"Your {self.vehicalName} is parked")

  def remove_vehicle(self):
    print(f"Your vehicle {self.vehicalName} is remove")

  def show_status(Self):
    print(f"Your vehicle {Self.vehicalName} is succesfully parked")

class Car(vehicle):
  def __init__(self, vehicalName, carType):
    super().__init__(vehicalName)
    self.carType = carType

  def add_car(self):
    print(f"added your car: {self.carType}")

class Bike(vehicle):
  def __init__(self, vehicalName, bikeType):
    super().__init__(vehicalName)
    self.bikeType = bikeType

  def add_bike(self):
    print(f"added your bike : {self.bikeType}")


car1 = Car("Honda","sedan")
bike1 = Bike("hyundi", "super bike")


car1.vehical_Show()
car1.park_vehicle()
car1.remove_vehicle()
car1.show_status()
