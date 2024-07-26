'''
Write a program to search a given element and prints its index
Input : [1,2,43,5,66,87,9]
Search = 43
Output : index = 2
'''

import array

arr=array.array('i',[])

num=int(input("Enter Size: "))

for i in range(num):
    ele=int(input())
    arr.append(ele)
print(arr)
search=int(input("Search Element: "))
print("index is:",arr.index(search))
