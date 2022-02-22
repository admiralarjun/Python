''' simple if else and elif...
if case1:
    perform action1
elif case2:
    perform action2
else: 
    perform action 3
'''
# For loops statements
''' general form
for item in object:
    statements to do stuff
'''
from re import T

num = int(input('Enter the number: '))
# num = 11
flag = None
for i in range(2,num-1):
    if(num%i==0):
        flag = True
        break
if(flag==True):
    print('Not a prime')
else:
    print('Prime')                
