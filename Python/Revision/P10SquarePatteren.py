#  Square Patteren
rows=int(input("Enter Rows:"))
cols=int(input("Enter Columns:"))

num=1

for i in range(rows):
    for j in range(cols):
        print(" ",num*num," ",end=" ")
        num=num+1
    print()


    """ 
Output:-
     1  4  9
     16 25 36
     49 64 81

"""
