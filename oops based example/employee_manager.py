#  Create a simple Employee-Manager hierarchy
# Employee base class

# Manager → inherits and adds team_size

# Override display_info() for each

class Employee:
  def __init__(self, name, id, position):
    self.name = name 
    self.id = id
    self.position = position

  
  def show_employee(self):
    print(f"employee name: {self.name} id is:{self.id} and position:{self.position}")

# inherit from employee
class Manager(Employee):
  def __init__(self, name, id, position, teamSize):
    super().__init__(name, id, position)
    self.teamSize = teamSize


  def manage_teamSize(self):
    print(f"team size managed by {self.name} : {self.teamSize}")

# override show employee 
  def show_employee(self):
    super().show_employee()
    print(f"Team Size is : {self.teamSize}")


manager1 = Manager("Ajay","12","Team lead","8")

# call Method
manager1.show_employee()
manager1.manage_teamSize()

