'''
Construct an immutable array of bytes from:
 |    - an iterable yielding integers in range(256)
 |    - a text string encoded using the specified encoding
 |    - any object implementing the buffer API.
 |    - an integer
'''

# bytes  is immutable
# byte must be in range(0,255)


data=[5,25,150,123,250]

print(data[0])             #5
print(data[1])             #25
print(data[2])            #150
print(data[3])            #123
print(data)              #[5, 25, 150, 123, 250] s
data1=bytes(data)
print(type(data1))       # <class 'bytes'>
print(type(data1[0]))     #<class 'Int>'>

data1[2]=180       #TypeError: 'bytes' object does not support item assignment
print(data1[2])                    



