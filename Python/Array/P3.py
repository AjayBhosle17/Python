# sum

import numpy

rows=int(input("Enter rows: "))
cols=int(input("Enter cols: "))
plane=int(input("Enter cols: "))

arr=numpy.zeros((plane,rows,cols),int)
sum=0
max=0
for i in range(plane):
    for j in range(rows):
        for k in range(cols):
            ele=int(input("Enter elements: ")
            #arr[i][j][k]=ele
            sum+=ele  
            #if arr[i][j][k]>max:
             #   max=arr[i][j][k]
            #print(max)            
                              

print(arr)
'''
print("Sum is: ",sum)

print("max is : ",max)
print("min is : ",min)

cnt=rows*cols            
print("count is: ",cnt)

mean=sum//cnt
print("mean is: ",mean)
'''
    
