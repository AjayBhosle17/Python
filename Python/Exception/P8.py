def fun():
    print("Start fun")
    print(10/0)
    print("End main")

print("start code")

try:
    fun()
except ZeroDivisionError:
    print("Zero nkos deus")

print("End Code")
