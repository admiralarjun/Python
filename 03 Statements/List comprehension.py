from hashlib import new

''' traditional way
list = []
for letter in 'sentence':
    list.append(letter)
print(list)    
'''

# comprehensive way
print("Making string into list.....")
neewList = [letter for letter in 'Test String']
print(neewList)
print("- - - - - - - - - -")

# mathematically its like
# x : x in {0,1,2,3,....10}
print("Printing square of nums within range and store in list...")
squareNums = [x**2 for x in range(0,11)] 
print(squareNums)
print("- - - - - - - - - -")
print("Even numns in range...")
evenNums = [num for num in range(0,11) if num % 2 == 0]
print(evenNums)
print("- - - - - - - - - -")
# list of celcius converting into farenheit
celcius = [0,10,20,56.23]

farenheit = [(temp*(9/5)+32) for temp in celcius]
print(farenheit)
 # nested list comprehension

parent = [x**2 for x in [x**2 for x in range (0,11)]]
print(parent) # we will get powers of 4
parent1 = [x**4 for x in range(11)] # to verify above
print(parent1)