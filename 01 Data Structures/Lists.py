numList = [1,2,3,4,5,6,7,8,9,10] # list of numbers seperated with comma
x=5
mixedList = ['string',23,23.45,'o'] # we can put all in list
StringList=['one','this','not','two']
print("list size is:",len(mixedList))
print(mixedList) # prints entire list
print(numList[0]) # contains index
print(numList[::-1]) # revering the numlist
print(mixedList*2) # prints entire list multiply 2
# --------
odd = [1,3,5]
even = [2,4,6]
sortIt = ['a','x','z','b','t']
sortItNums = ['2','4','1','5']
sortIt.sort() # sorts in ascending order of alphabets
sortItNums.sort() # sorts nums
print(sortIt) 
print(sortItNums)
sortIt.reverse() # reversing
print(sortIt)
print(*sortIt) # printing without square brackets
List1=[1,2,3]
List2=[4,5,6]
List3=[6,7,8]
Matrix=[List1,List2,List3] # list of lists
print(Matrix[2][2]) # 2nd index of row and column, works as matrix