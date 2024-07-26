'''
Write a program to find duplicates from the array
Input : [1,1,3,4,5,6,6]
Output : 1 6
'''
import array

arr=array.array('i',[])

num=int(input("Enter Size: "))

for i in range(num):
    ele=int(input())
    arr.append(ele)
print(arr)

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]==arr[j]):
            print(arr[j])
