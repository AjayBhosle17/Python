'''
Write a program which accepts sentences from the user
and print a number of words of even and odd length from that
sentence.
Input: In my company
Output: Even: 2 Odd:1
'''
str1=input("ENter String: ")
even=0
odd=0

str2=str1.split(' ')
for i in str2:
    if(len(i)%2==0):
        even+=1
    else:   
        odd+=1
print()   
print(even)
print(odd)
