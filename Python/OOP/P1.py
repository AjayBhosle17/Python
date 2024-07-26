#instance variable

class Student:
    def __init__(self,name,stud_id):
        self.name=name
        print("In constructor1")
        self.stud_id=stud_id
    def __init__(self,name,stud_id):
        self.name=name
        print("In constructor2")
        self.stud_id=stud_id
    def DisplyData(self):
        print(self.name)
        print(self.stud_id)

print("Enter Student1 Data")
name=input("Enter Name: ")
stud_id=int(input("Enter Id: "))

obj1=Student(name,stud_id)
obj1.DisplyData()

print("Enter Student2 Data")
name=input("Enter Name: ")
stud_id=int(input("Enter Id: "))

obj2=Student(name,stud_id)
obj2.DisplyData()


