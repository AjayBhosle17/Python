# user input use numpy

from numpy import *

num=int(input("Enter no of elements: "))

a=ones(num,dtype=int)

print(a)
for i in range(len(a)):

    ele=int(input("Enter element: "))
    a[i]=ele

print(a)


