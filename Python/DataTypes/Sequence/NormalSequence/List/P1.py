# list(iterable=(), /)
   
#Built-in mutable sequence.
   
  #1. If no argument is given, the constructor creates a new empty list.
  #2. The argument must be an iterable if specified.
   



z='A'
y=20

list1=[10,20,'A']
list2=[10,20,'A']

x=10

print(z)                           # 'A'
print(y)                           # 20

print(type(list1))                 #<class 'list'>
print(type(list2[0]))              #<class 'int'>
print(x)                            #10
print(list1[2])                     #'A'
print(list2[0])                     #10
print(id(list1[0]))     # Address   #100
print(id(list1[1]))                 #200
print(id(list2[0]))                 #100
print(id(list2[1]))                 #200




