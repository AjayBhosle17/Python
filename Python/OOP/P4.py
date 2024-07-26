class Cric:
    matchformat='T20'
    def __init__(self):
        self.name='Dhoni'
        self.jerNo=7

    #decor
    def myclassmethod(fun):
        def inner(*args):
            fun(args[0].__class__)
        return inner

    #instance method

    def disp(self):
        print("Name={} and JerNo={}".format(self.name,self.jerNo))

    #classmethod
    @myclassmethod
    def dispformat(cls):
        print(cls)
        print(cls.matchformat)

player1=Cric()
player1.disp()

print(player1)
player1.dispformat()


