'''
Write a program which accepts string from the user and
searches for the first occurrence of a specific character in string and
returns the position at which character is found (Implement strchr()).
Input: India is my country.
Enter Char : m
Output: Character m is found at position 9

'''

flag=0
str1=input("Enter String: ")

search=input("Serach charcter: ")

for i in range(len(str1)):
    if(search==str1[i]):
        flag=1
        print("charcter ",search,"is found at position",i)
        break
          

