#sum

def sum(x):
    sum=0
    print(id(x))
    for i in range(x+1):
        sum+=i
    print(sum)



num=int(input("Enter Num: "))
sum(num)

