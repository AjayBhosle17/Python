num=int(input("Enter A number\n"))
sum=0

for i in range(1,num):
    if(num%i==0):
        sum+=i
if(sum==num):
    print(num," is perfect number")
else:
    print(num," is not perfect number")
