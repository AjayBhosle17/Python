'''
Write a program to find min and max from the given array
Input : [1,43,65,71,89,55]
Output : min = 1 '''


import array
arr=array.array("i",[])

num=int(input("enter size of elements: "))

for i in range(num):
    ele =int(input())
    arr.append(ele)
print(arr)

print("min is: ",min(arr))
print("max is: ",max(arr))
