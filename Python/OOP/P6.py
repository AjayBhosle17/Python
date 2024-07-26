class Cric:
    matchformat='T20'

    def __init__(self):
        self.name='Virat'
        self.jerNo=18

    #decor

    def myclassmethod(fun):
        def inner(*args):
            fun(args[0].__class__)
        return inner

    #instance method

    def disp(self):
        print("Name={} and JerNo={}".format(self.name,self.jerNo))


@myclassmethod
def dispformat(cls):
    print(cls)
    print(cls.matchformat)

@staticmethod

def demo():
    print("static method")

player1=cric()
player1.disp()
print(player1)
player1.demo()
player1.dispformat()
