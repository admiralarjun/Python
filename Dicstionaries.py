# unlike index, where each elements is accessed by a number
# in dictionary we use something called 'key' to identify elements

D1 = {'inte':123,'key1':'value','key2':'value2'}
# print(D1[0]) - won't work coz we need to specify the key
print(D1['key2']) # value of key2 will be printed
print(D1['key2'][::-1]) # all this kind of operations can be done
print(D1['key1'].upper()) # can peroform all sort of methos
print(D1['inte'] - 120) # can perform arithematic operations too
D1['inte'] -= 120 # it will update the dictionary
print(D1['inte'])
d = {} # created empty dictionary
print(d) # empty {} will be printed
d['animal'],d['pet'] = 'dog','parrot' # these values will go into dictionary
print(d) # prints {'animal': 'dog', 'pet': 'parrot'}
print(*d) # prints only the keys
print(d.values()) #.values, .keys, like more methods are there
# nested dictionaries ------->
d1 = {'dic':{'subDic':{'subDic2':'123'}}}
print(d1['dic']['subDic']['subDic2']) # prints 123

