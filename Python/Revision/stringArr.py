import array
import numpy

def fun(str2,arr2):
        for i in range(len(str2)):    
            if(len(str2[i]) %2 ==0):
                arr2.append(i)
        return arr2        
        #print("String is ",x)
            
        
num=int(input("Enter no of string: "))

arr1=numpy.array([])
arr2=array.array('i',[])
for i in range(num):
    num1=input("Enter string: ")
    
    arr1=numpy.append(arr1,num1)
print(arr1)

index=fun(arr1,arr2)
print(index)

