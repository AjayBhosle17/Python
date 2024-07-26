'''
Write a program to reverse a array
Input : [1,2,3,4,5]
Output : [5,4,3,2,1]
'''

import array

arr=array.array('i',[])

num=int(input("Enter Size: "))

for i in range(num):
    ele=int(input())
    arr.append(ele)
print(arr)
arr.reverse()
print("Reverse Array is: ",arr)
