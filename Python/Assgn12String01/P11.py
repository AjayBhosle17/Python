'''
Write a program to convert the string from lowercase to
uppercase (Implement strupr()).
Input: DevIce DriVer
Output: DEVICE DRIVER

'''

str1=input("Enter string: ")
str2=""
i=0

while(i<len(str1)):
    if(ord(str1[i])>=97 and (ord(str1[i])<=122)):
        x=(ord(str1[i])-32)
        str2=str2+chr(x)
    else:
        str2=str2+str1[i]
    i+=1    
     
         
print(str2)
