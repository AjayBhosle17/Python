'''
Write a program which accepts sentences from the user
and print a number of small letters, capital letters and digits from that
sentence.
Input: abcDE 5Glm1 O
Output: Small:5 Capital: 4 Digits: 2
'''

str1=input("Enter String: ")

small=0
capital=0
digit=0

for i in range(len(str1)):
    if(str1[i]>='a' and str1[i]<='z'):
        small+=1
    if(str1[i]>='A' and str1[i]<='Z'):
        capital+=1
    if(str1[i]>='1' and str1[i]<='9'):
        digit+=1

print(small)
print(capital)
print(digit)

        



