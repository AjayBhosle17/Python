''' 
Write a program to find the occurrence of a given number from
the array
Input : [1,2,3,4,4,5,6,7]
Occurrence count of number = 4
Output: 2 '''

import array
arr=array.array("i",[])

num=int(input("enter size of elements"))

for i in range(num):
    ele =int(input())
    arr.append(ele)
print(arr)

num1=int(input("Which number u want count of occurrence: "))
print(arr.count(num1))


