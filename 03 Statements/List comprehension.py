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


