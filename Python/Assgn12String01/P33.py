'''
Write a program which accepts string from user and
search last occurrence of specific character in string and return the
position at which character is found (Implement strchr()).
Input: India is my country.
Enter char : n
Output: Character n is found at position 15
'''

flag=0

str1=input("Enter String: ")

search=input("Enter last charcter to search: ")

i=0
x=0

while(len(str1)>i):
    if(search==str1[i]):
        flag=1
        x=i
    i+=1
if(flag==1):
    print("Index is: ",x)

