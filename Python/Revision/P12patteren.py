rows=int(input("Enter a rows"))
cols=int(input("Enter a cols"))

num1=65
num2=1

for i in range(rows):
    if(i==1):
        for j in range(cols):
            print("*",end=" ")

    if(i%2!=0):
        for j in range(cols):
            print("*",end=" ")
            char=chr(num1)
            print(char,end=" ")
            num1+=1
    if(i%2==0):
        for j in range(cols):
            print("*",end=" ")
            print(num2,end=" ")
            num2+=1
    if(i%3==0):
        for j in range(cols):
            print("*",end=" ")
           
    print()    


