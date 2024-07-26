def concat(fun):
    def inner(str1,str2):
        if(len(str1)==len(str2)):
            fun(str1,str2)
            return str1+str2
        else:
            return "String length is not equal"
    return inner

def anagram(fun):
    def inner(str1,str2):
        flag=0
        len1=len(str1)
        for i in range(len1):
            for j in range(len1):
                if(str1[i]==str2[j]):
                    flag=1
                    break
            if(flag==0):  
                flag=1
                break
        if(flag==1):
            return 'not anagram'
        else:
            return 'anagram'
    return inner

@concat
@anagram
def string(*strings):
    return strings

str1=input("Enter String: ")
str2=input("Enter String: ")
print(string(str1,str2))

