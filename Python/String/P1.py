# Methods in string classes

#1.count()

str1=input("Enter String: ")
cnt=0
i=0
search=input("Enter Charcter to search: ")

while(len(str1)>i):
    if(search==str1[i]):
        cnt+=1
    i+=1
print(search ," charcter count is ",cnt)    



#2.capitalize

str2=input("Enter String: ")
for i in range(len(str2)):
    if(str2[i]>'a' and str2[i]<='z'):
        str2[i]=str2[i]-'a'

print(str2)
