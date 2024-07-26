#tuple(iterable=(), /)
 
# Built-in immutable sequence.
 
 # 1. If no argument is given, the constructor returns an empty tuple.
 # 2. If iterable is specified the tuple is initialized from iterable's items.
 # 3. If the argument is a tuple, the return value is the same object.

dataList=['Dhoni',7,50,33]
dataTuple=['Virat',18,52,33]

print(type(dataList))     #<class 'str'>
print(type(dataTuple))    #<class 'str'>

dataList[2]=60.77
dataTuple[2]=02.22

print(dataList[2])           # 60.77
print(dataTuple[2])           #02.22  
print(dataList)             #['Dhoni', 7, 60.77, 33]
print(dataTuple)            # ['Virat',18,02.22,33]
