# Capitalize 

def mycapitalize(str1):
    str2=''

    if (str1[0]>'a' and str1[0]<='z'):
        str2=chr(ord(str1[0])-32)+str1[1:]
    
    return str2   



str1=input("Enter String: ")
mycapitalize("str1")

str2=input("Enter String: ")
print(mycapitalize(str2))

print(mycapitalize(str1))
