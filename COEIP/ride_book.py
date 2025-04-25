

class RideBook:
   def __init__(self, ride_name, pickup, location):
      self.ride_name = ride_name
      self.pickup = pickup
      self.location = location

   def  start_ride(self):
      print(f"Starting ride {self.ride_name} from {self.pickup} to {self.location}")
  
start1 = RideBook("Ajay", "vivek vihar", "mansarover")
start1.start_ride()