'''
Write a program to swap two consecutive numbers in the array
Input : [1,2,3,4,5,6,7,8]
Output:[2,1,4,3,6,5,8,7]
'''

import array

arr=array.array('i',[])

num=int(input("Enter Size: "))

for i in range(num):
    ele=int(input())
    arr.append(ele)
print(arr)

for i in range(0,len(arr),2):
    x=arr[i]
    arr[i]=arr[i+1]
    arr[i+1]=x
print(arr)

