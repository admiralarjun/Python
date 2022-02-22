from turtle import clear
import os

tup = (2,4,6,8,10)
tup1 = [(10,2),(5,4),(6,4)]
'''
for i in tup:
    print(i) # print elements iteratively inside the tuple
'''
# tuple unpacking
for (j,k) in tup1:
    # print(j) - prints 1st value of the pair
    # print(j,k) - prints both value of pair
    # print(k)  prints 2nd value
    print(k-j) # operations are also possible

