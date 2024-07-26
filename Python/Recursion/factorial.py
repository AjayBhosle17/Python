def fact(num):
    if( num==1):
        return 1
    else:
        return num*fact(num-1)

num=int(input("Enter number: "))
print(id(num))
x=fact(num)
print(id(x))
print(x)

