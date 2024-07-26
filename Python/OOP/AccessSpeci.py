class Demo:
    def __init__(self):
        self.x=10
        self._y=20
        self.__z=30

    def fun(self):
        print(self.x)
        print(self._y)
        print(self.__z)

obj1=Demo()           
obj1.fun()           # 10 #20 #30
print(obj1.x)        # 10
print(obj1._y)       #20
#print(obj1.__z)      #Error
print(obj1._Demo__z)  #30
print(dir(obj1))     #directries

