class std:
    srn=0
    name="noname"
    stu_class="noclass"
    elective=[]


    def __init__(self,name,srn,stu_class):
        self.srn = srn
        self.name = name
        self.std_class = stu_class

    def add_elective(self,subject):
       self.elective.append(subject)

s=std("Ram",123,"2.1")

print(f"{s.srn=}")
print(f"{s.name=}")
print(f"{s.stu_class=}")