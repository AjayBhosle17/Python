x=2

try:
    print("In try ")
    print(10/x)
except ZeroDivisionError:
    print("In Except")
else:
    print("In Else")

finally:
    print("Always Here")
