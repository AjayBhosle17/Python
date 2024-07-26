# Dictonary have "key" and "value"

dictData={18:"Virat",7:"Dhoni",45:"Rohit",17:"AB"}

print(dictData)                  #{18: 'Virat', 7: 'Dhoni', 45: 'Rohit', 17: 'AB'}
print(type(dictData))            #<class 'dict'>


print(dictData[17])              # AB
print(dictData["Virat"])         # KeyError: 'Virat'
