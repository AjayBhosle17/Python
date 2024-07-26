# bytearray  is mutable
# bytearray must be in range(0,255)

data1=[5,25,150,123,250]

data=bytearray(data1)     # ByteArray Convert

print(data[0])            #5
print(data[1])            #25
print(data[2])            #150
print(data[3])            #123
print(data)               #  Address
print(type(data))         # <class 'bytearray'>
print(type(data[0]))      #<class 'int'>

data[2]=180
print(data[2])            #180 
 
