class Parent(object):
    x=10
    def __init__(self):
        print("Parent Constructor")
        self.y=20
    @classmethod
    def show(cls):
        print(cls.x)
    
    def disp(self):
        print(self.x)
        print(self.y)

class Child(Parent):
    def __init__(self):
        print("Child Constructor")
        super().__init__()
    def ChildDisp(self):
        print(self.x)

obj=Child()          #Child Constrctor   #Parent Constrctor
obj.ChildDisp()      #10
obj.show()           #10
obj.disp()           #10  #20


