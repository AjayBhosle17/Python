def fun():
    print("In fun")
    
    try:
        print(10/0)
    except ZeroDivisionError:
        print("Zero nkos deus")
        print("End main")


print("start code")
fun()
print("End Code")
