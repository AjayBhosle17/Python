'''
Write a program which accepts sentences from the user
and print a number of white spaces from that sentence.
Input: In my company
Output: 2
'''

str1=input("Enter String: ")
cnt=0
for i in range(len(str1)):
    if(ord(str1[i])==32):
        cnt=cnt+1
print()
print(cnt)
