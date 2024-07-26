i=3
def myfun():
    global i 
    print("ajay",i)
    i+=1
    myfun()

myfun()
