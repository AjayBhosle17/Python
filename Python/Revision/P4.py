
flag=1
while(flag):
    student1=int(input("Enter Marks\n"))
    student2=int(input("Enter Marks\n"))
    student3=int(input("Enter Marks\n"))

    if((student1>student2) and (student1>student3)):
        print("Student1 ",student1," is Highest mark compare to Student2 and Student3\n")
    
    elif((student2>student1) and (student2>student3)): 
        print("Student2 ",student2," is Highest mark compare to Student1 and Student3\n")
    
    elif((student3>student1) and (student3>student2)):
        print("Student3 ",student3," is Highest mark compare to Student1 and Student2\n")
    
    else:
        print("Equal marks for student1,student2,student3")
    
    flag=int(input("Do you want to continue : (Enter for Yes(1) or Enter for  No(0))\n")) 
