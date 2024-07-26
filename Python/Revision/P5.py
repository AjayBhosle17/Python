x=int(input("Enter Starting number\n"))
y=int(input("Enter Ending number\n"))

cnt=0
for i in range(x,y+1):
    if((i%4==0 and i%5==0) or (i%6==0 and i%7==0)):
        cnt+=1
        print(i)

print("count= ",cnt)
    
        

