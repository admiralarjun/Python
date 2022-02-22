# unordered collections of "Unique elements" is Set
x = set()
x.add(2)
print(x) # output is with {} similar to dictionary
# its not dictionary, but imagine if it have only keys
x.add(3)
print(x)
x.add(3) # 3 is already there, so nothing will happen
l = [1, 2, 3, 1, 2, 3, 4, 5, 6, 4, 5, 6]
print(set(l)) # set casting prints each elements only once
