'''
Write a program to find odd numbers from the array
Input : [1,2,3,5,7,9,12]
Output : 1 3 5 7 9
'''
import array

arr=array.array('i',[])

num=int(input("enter size of array: "))

for i in range(num):
    ele=int(input())
    arr.append(ele)

print (arr)   

for x in arr:                            #        x=arr[0]
    if(x%2==1):
        print(x,end=' ')
print()      


'''
Output:
array('i', [1, 2, 3, 4, 5])
1 3 5
'''
