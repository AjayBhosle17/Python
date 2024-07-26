'''
Write a program to convert the string from upper case to
lower case (Implement strlwr()).
Input: DevIce DriVer
Output: device driver

'''

str1=input("Enter string: ")
str2=""
i=0

while(i<len(str1)):
    if(ord(str1[i])>=65 and (ord(str1[i])<=90)):
        x=(ord(str1[i])+32)
        str2=str2+chr(x)
    else:
        str2=str2+str1[i]
    i+=1    
     
         
print(str2)
