# WAP find even numbers from the array


import array

arr=array.array('i',[])

num=int(input("Enter Number: "))

for i in range(num):
    ele=int(input("Enter num"))
    arr.append(ele)

    if(ele%2==0):
        print(ele,end=" ")

