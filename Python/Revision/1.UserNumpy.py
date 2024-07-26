import numpy

myArray=numpy.array([])

a=int(input("size"))

for i in range(a):
    x=int(input("Element"))
    numpy.append(x)
myarray=numpy.array(myArray)    
print(numpy.floor(myarray))    

