x=int(input("Enter Starting number\n"))
y=int(input("Enter Ending number\n"))

cnt=0
while(x < y+1):
    if((x%4==0 and x%5==0) or (x%6==0 and x%7==0)):
        print(x)
        cnt+=1
    x+=1

print("count=",cnt)
