# in byte array range will be(0,256)

data1=[5,25,150,2795678,250]

print(data1)

data=bytearray(data1)

print(data)                  #ValueError: byte must be in range(0, 256)


