'''
Write a program to sum alternate number from the given array
Input : [1,2,3,4,5,6,7]
Output : 16
/// 1 + 3 + 5 + 7
'''
import array

arr=array.array('i',[])

num=int(input("Enter array size: "))

for i in range(num):
    ele=int(input())
    arr.append(ele)
print(arr)

sum=0
for x in arr:
    if(arr.index(x)%2==0):
        sum+=x
print(sum)
