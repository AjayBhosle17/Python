def palindrone(fun):
    def inner(x):
        if x==int(fun(x)):
            return True
        else:
            return False
    return inner

def reverse(fun):
    def inner(x):
        str1=str(x)
        return str1[-1::-1]
        
    return inner

@palindrone
@reverse
def num2(x):
    return x
x=int(input("Enter Number: "))
if num2(x):
    print(x,"is palindrone")
else:
    print(x,"is not palindrone")

