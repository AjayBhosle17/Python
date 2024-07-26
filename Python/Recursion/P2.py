
def sum(num):
    
    if(num==1):
        return 1
    else:
         return num+sum(num-1)  
p=int(input())
x=sum(p)
print(x)
