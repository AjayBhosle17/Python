'''
Write a program which accepts string from the user and
then reverse the string till first N characters without taking another
string.
Input: Hello World
N : 5
Output: olleH World
'''

str1=input("Enter String: ")
str2=''
num=int(input("how many first charcters reverse"))
str2=str1[0:num]
str3=str2[-1:-num-1:-1]+str1[num:]

print(str3)
