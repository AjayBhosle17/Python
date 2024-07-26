'''
Write a program which accepts strings from the
user and copy first N characters into some destination string
(Implement strncpy()).
Input: India is my Country
N : 8
Output: India is

'''

str1=input("ENter String: ")
str2=''
num=int(input("how many numbers you want first: "))
str2=str1[0:num]
print(str2)
