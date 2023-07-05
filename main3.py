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

male_student = ["stuM1","stuM2","stuM3","stuM4","stuM5"]
female_student = ["stuF1","stuF2","stuF3","stuF4","stuF5"]
students = []
for student_name in male_student:
  students.append(Student(student_name,18,"male"))
for student_name in female_student:
  students.append(Student(student_name,18,"female"))
for student in students:
  student.info()