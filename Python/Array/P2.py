# sum

import numpy

rows=int(input("Enter rows: "))
cols=int(input("Enter cols: "))

arr=numpy.zeros((rows,cols),int)
sum=0
max=0
cnt=0

for i in range(rows):
    for j in range(cols):
        ele=int(input("Enter elements: "))
        arr[i][j]=ele
        min=arr[0][0]
        sum+=arr[i][j]   
        if arr[i][j]>max:
            max=arr[i][j]
             
        if arr[i][j]<min:
            min=arr[i][j]
          

print(arr)
print("Sum is: ",sum)

print("max is : ",max)
print("min is : ",min)

cnt=rows*cols            
print("count is: ",cnt)

mean=sum//cnt
print("mean is: ",mean)

    
