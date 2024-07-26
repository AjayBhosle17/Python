# class Variables

class Cafe:
    menucard=1
    def __init__(self,dish):
        self.dish=dish
    def order(self):
        print(self.dish)
        print(self.menucard)
obj1=Cafe("Burger")
obj2=Cafe("largeFries")
obj1.menucard=0
obj1.order()
#obj1.menucard=0

#obj2=Cafe("largeFries")
obj2.order()

