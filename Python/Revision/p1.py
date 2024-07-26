dictionary={}
def addtoc(c):

    if i in c:
        c[i]+=1
    else:
        c[i]=1

addtoc('China')
addtoc('Japan')
addtoc('china')
print(len(c))
