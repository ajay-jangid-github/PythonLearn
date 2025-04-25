
# class Ride:
#   def __init__(self, ride_name, pickup, destination):
#     self.ride_name = ride_name
#     self.pickup = pickup
#     self.destination = destination
#     self.ride_status = "Pending"

#   def start_ride(self):
#         print(f"Ride started for {self.ride_name} from {self.pickup} to {self.destination}")
    

# # now we create an object of the class Ride

# ride1 = Ride("Ajay" ,"Vivek Vihar", 'Mansarover Park')
# ride1.start_ride()

class Ride:
    def __init__(self, ride_name, pickup, destination):
        self.ride_name  = ride_name
        self.pickup = pickup
        self.destination = destination
    
    def start_ride(self):
        print(f"Ride started for {self.ride_name} from  {self.pickup} to  {self.destination}")
  

start1  = Ride("ajay" ,"vivek vihar", "manasarover")
start1.start_ride()