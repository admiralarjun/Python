# immutable list is kinda tuple lol
# we cannot reassign items in the tuples
tuple1 = (1,2,3) # unlike lists, here its normal brackets instead of square
# all slicing,indexing operations are allowed
print(tuple1.index(2)) # prints index 2
print(tuple1.count(1)) # shows how many times 1 is stored

# tuple1[0] = 5 
# TypeError: 'tuple' object does not support item assignment#
