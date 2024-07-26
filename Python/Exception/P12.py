def fun():
    
    flag=0

    while(flag!=1):
        try:
            x=int(input("Enter Value "))
            flag=1
        except ValueError:
            print("Enter Integer value ")

        except EOFError:
            print("Enter Integer valueError ")

    

print("Start main")
fun()

print("End main")
