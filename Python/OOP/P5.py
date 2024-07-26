class Cric:
    matchformat='T20'
    def __init__(self):
        self.name='Dhoni'
        self.jerNo=7
#instance method
    def disp(self):
        print("Name={} and JerNo={}".format(self.name,self.jerNo))

    #classmethod
    @classmethod
    def dispformat(cls):
        print(cls)
        print(cls.matchformat)

player1=Cric()
player1.disp()

print(player1)
player1.dispformat()


