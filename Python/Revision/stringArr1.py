
import numpy

def fun(str2):
    for i in arr1: 
        for x in str2:
            cnt=0
            for y in range(len(x)):
                cnt+=1
            
        if(cnt %2 ==0):
            print("string is ",x)
            
        

num=int(input("Enter no of string: "))

arr1=numpy.array([])

for i in range(num):
    num1=input("Enter string: ")
    
    arr1=numpy.append(arr1,num1)
print(arr1)

fun(arr1)
