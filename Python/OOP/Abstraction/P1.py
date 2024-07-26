from abc import ABC,abstractmethod

class Amazon(ABC):
    @abstractmethod
    def product(self):
        pass
        #print("Nice Quality1")
        

    def employees(self):
        print("35 employees work on front page of amazon")
class AWS(Amazon):
    def product(self):
        print("Nice Product")
    def security(self):
        print("Flexible security")
obj1=AWS()
obj1.product()
obj1.employees()
obj1.security()

