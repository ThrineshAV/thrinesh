class Student:
  def __init__(self,name,age,gender):
    self.name = name
    self.age = age
    self.gender = gender

  def info(self):
    print("student details")
    print(f"Name : {self.name}")
    print(f"age : {self.age}")
    print(f"gender : {self.gender}")
    
    
ram = Student("ram",18,"male")
ram.info()