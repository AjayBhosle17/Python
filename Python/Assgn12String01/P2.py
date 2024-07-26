'''
Write a program which accepts a string from the user
which contains characters from ‘b’ to ‘y’.
Input: mn jn kn kazfd
Output: mn jn kn k
'''

str1=input("Enter String: ")
i=0
while(i<len(str1)):
    if(((ord(str1[i]))>=66 and (ord(str1[i])<=89)) or((ord(str1[i]))>=98 and (ord(str1[i])<=121))  or ((ord(str1[i]))==32)):
        print(str1[i], end = "")
        i+=1
    else:
        break
