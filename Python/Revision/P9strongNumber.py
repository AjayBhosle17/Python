# Check Strong or not strong Number

sum=0
num=int(input("Enter A number\n"))

temp=num

while(num):
    i=1
    fact=1

    rem=num%10

    while(i<=rem):

        fact=fact*i

        i=i+1

        sum=sum +fact

        num=num//10

if(sum==temp):
    print(sum," is strong number\n")

else:
    print(sum," is not a strong number ")



