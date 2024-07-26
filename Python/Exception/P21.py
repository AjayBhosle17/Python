def fun(x):
    try:
        y=int(input("Enter Num: "))

        try:
            print(x/y)
        except ValueError:
            print("Zero nkos deu")
    except (EOFError,ZeroDivisionError,ValueError,Exception):
        print("plz enter Integer value")


fun(10)
