try:
    print("In Outer try")
    #print(10/0)

    try:
        print("in inner try");
        print(10/0)
    
    except ValueError:
        print("In InnerExcept")

    finally:
        print("Inner Finally")

except ZeroDivisionError:
    print("In OuterException")

finally:
    print("In Outer try")
