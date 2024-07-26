'''
Write a program to find even numbers from the array
Input : [1,2,3,4,6,8,10]
Output : 2 4 6 8 10
'''
import array

arr=array.array('i',[])

num=int(input("enter size of array: "))

for i in range(num):
    ele=int(input())
    arr.append(ele)

print (arr)   

for x in arr:
    if(x%2==0):
        print(x,end=' ')
print()        
