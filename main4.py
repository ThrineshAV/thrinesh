class Student:
  college_name="REVA UNIVERSITY"
  def __init__(self,name,age,gender):
    self.name = name
    self.age = age
    self.gender = gender

  def info(self):
    marks=[1,2,3,4,5]
    self.college()
    print("student details")
    print(f"Name : {self.name}")
    print(f"age : {self.age}")
    print(f"gender : {self.gender}")
    self.total_marks(marks)
  #classmethod
  @classmethod
  def college(cls):
    print(f"collge: {cls.college_name}")
  #staticmethod
  @staticmethod
  def total_marks(marks_list):
    total=0
    for mark in marks_list:
      total = total + mark
    print(f"totalmarks = {total}")
    return total
  
ram = Student("ram",18,"male")
ram.info()