class A:
    def method(self):
        print("A class method is Called")

class B(A):
    def method(self):
        print("B class method is Called")

class C(A):
    def method(self):
        print("C class method is Called")

class D(B,C):
    def method(self):
        print("D class method is Called")
        B.method(self)
       # A.methodi(self)
        C.method(self)
       # D.method(self)          #recursive call
        

obj=A()
obj.method()
