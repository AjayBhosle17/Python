class employee:
    
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal

    def info(self):
        print(self.name)
        print(self.sal)

emp=employee("Ashish",50.00)

emp.info()

try:
    emp.disp()
except AttributeError:
    print("Disp Attractive Nahiye-1")
except Exception:
    print("Disp Attractive Nahiye-2")
except IndexError:
    print("Disp Attractive Nahiye-3")

print("End Code")
