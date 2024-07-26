'''
Write a program which accepts string from the user and
then reverse the string till the last N characters without taking
another string.
Input: Hello World
N : 5
Output: Hello dlroW
'''

str1=input("Enter String: ")
str2=''
num=int(input("how many first charcters reverse"))

str2=str1[0:]+str1[-1:-num-1:-1]

print(str2)
