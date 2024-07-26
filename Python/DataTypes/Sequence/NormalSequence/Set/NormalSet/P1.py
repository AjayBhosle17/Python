# By Default Dictonary {} Set asto.
# Duplicate data not print
data={10,20,30}

print(data)                      #{10,20,30}
print(type(data))                #<class 'set'>


data1={10,20,30,10.4,'a',6}
print(data1)                  #{6,'a',10,20,30}
print(type(data1))            #<class 'set'>
