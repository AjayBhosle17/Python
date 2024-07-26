'''
Write a program which accepts sentences from the userand prints a number of words from that sentence.
Input: In my company
Output: 3
'''

str1=input("Enter string: ")
cnt=0
for i in range(len(str1)):
    if(str1[i]==' '):
        cnt+=1
print()

print(cnt+1)
