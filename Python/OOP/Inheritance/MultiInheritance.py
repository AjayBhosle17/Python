
class Z:
    def __init__(self):
        super().__init__()
        print("Z constructor")
class X(Z):
    def __init__(self):
        super().__init__()
        print("X constructor")
class Y(Z):
    def __init__(self):
        super().__init__()
        print("Y constructor")

class A:
    def __init__(self):
        super().__init__()
        print("A constructor")
class B(Y):
    def __init__(self):
        super().__init__()
        print("B constructor")
class C(X):
    def __init__(self):
        super().__init__()
        print(super())
        print("C constructor")
class D(A,B,C):
    def __init__(self):
        super().__init__()
        print(super())
        print("D constructor")

obj1=D()
print(D.mro())
