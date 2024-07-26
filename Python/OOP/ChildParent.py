class Parent:
    x=10
    def __init__(self):
        self.y=10

    def disp(self):
        print(self.x)
        print(self.y)
    @classmethod
    def show(cls):
        print(cls.x)
obj1=Parent()  
obj2=Parent()

obj1.x=50
obj1.disp()  #50 #10
obj2.disp()  #10 #10

Parent.x=80

obj1.disp()  #50 #10
obj2.disp()  #80 #10

obj1.x=80     
Parent.x=150

obj1.disp() # 80 #10
obj2.disp() #150 #10

obj1.show() #150
