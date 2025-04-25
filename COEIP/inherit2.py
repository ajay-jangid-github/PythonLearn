
class User:
  def __init__(self, userName, password):
    self.userName = userName
    self.password = password
  
  def show_profile(self):
    print(f"User: {self.userName}")
    print(f"Password: {self.password}")

class Student(User):
    def __init__(self,userName, password, studentID):
      super().__init__(userName, password)
      self.studentID = studentID

    def student_profile(self):
      print(f"studnetId: {self.studentID}")

student1 = Student("john doe", "123", "012")
student1.show_profile()
student1.student_profile()
