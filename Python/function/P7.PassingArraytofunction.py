# Passing array to function

import numpy

size=int(input("Enter num: "))

arr=numpy.zeros(size,int)

for i in range(size):
    val=int(input("Enter Number: "))
    arr[i]=val

x=sum(arr)  
print(x)
  
def sum(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum    

