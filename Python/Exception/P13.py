def fun(a,b):

    try:
        x=a/b
    except ZeroDivisionError:
        print("Divide by Zero")
    else:
        print(x * x)

try:
    a=int(input("Enter Value: "))
    b=int(input("Enter Value: "))
    
except ValueError:
    print("Enter Integer Value")

fun(a,b)
