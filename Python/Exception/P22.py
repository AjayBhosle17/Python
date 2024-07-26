class NoAccessToLeetCode():

    def __init__(self,msg):

        self.msg=msg

class Leetcode:

    def content(self):
        print("All Leetcode content : access")

class Bootcamp:

    def __init__(self,name,numProSolve):
        self.name=name
        self.numProSolve=numProSolve
    
    def checkCode(self,course):

        if self.numProSolve<600:
            raise NoAccessToLeetCode("{} ,you are not eligible to access Course".format(self.name))
        else:
            course.content()



ltcode=Leetcode()
btcamp=Bootcamp("Ajinkya",65)

try:
    btcamp.checkCode(ltcode)
except NoAccessToLeetCode as obj:
    print(obj)

print("End Code")
