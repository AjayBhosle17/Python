'''
Write a program which accepts strings from the user and
accept number N then copy the last N character into some other
string.
Input: India is my
N : 5
Output: is my
'''

str1=input("Enter String: ")

str2=''

num=int(input("how many accepts last charcters:"))

str2=str1[-1:-num-1:-1]
print(str2)
