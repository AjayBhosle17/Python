
flag=1
while(flag):
    student1=float(input("Enter Marks\n"))
    student2=float(input("Enter Marks\n"))
    student3=float(input("Enter Marks\n"))

    if((student1>student2) and (student1>student3)):
        print("Student1 ",student1," is Highest mark compare to Student2 and Student3\n")
    
    elif(student2>student3): 
        print("Student2 ",student2," is Highest mark compare to Student1 and Student3\n")
    
    else:
        print("Student3 ",student3," is Highest mark compare to Student1 and Student2\n")   
   
    flag=int(input("Do you want to continue : (Enter for Yes(1) or Enter for  No(0))\n")) 
