# class is a blueprint/template for creating objects

class LinkedIn:
  def __init__(self, company, position, location):
    self.company = company
    self.position = position
    self.location = location

    def __add__(self, other):
        return LinkedIn(self.company + " & " + other.company, self.position + " & " + other.position, self.location + " & " + other.location)

LinkedIn1 = LinkedIn("Google", "Software Engineer", "Mountain View, CA")
LinkedIn2 = LinkedIn("Microsoft", "Data Scientist", "Redmond, WA")
LinkedIn3 = LinkedIn1 + LinkedIn2 # This will not work as we have not defined __add__ method in the class

print(LinkedIn3.company) # 
print(LinkedIn3.position) # This will not work as we have not defined __add__ method in the class
print(LinkedIn3.location) # This will not work as we have not defined __add__ method in the class
# print(LinkedIn1.company)
# print(LinkedIn1.position)
# print(LinkedIn1.location)
  


