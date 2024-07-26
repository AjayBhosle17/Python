def sum_sub(x,y):
    sum=x+y
    sub=x-y
    return sum,sub 




x=int(input("Enter Numbers: "))
y=int(input("Enter Numbers: "))

result=sum_sub(x,y)
print(result)
print(type(result))

for i in result:
    print(i)
sum,sub=sum_sub(20,10) 
print(sum,sub)
