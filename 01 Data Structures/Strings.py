# from __future__ import division
from os import access

a='hello'
print(len(a))
print(a[0]) # a is kinda array and is elements are accessed by index
print(a[1:4]) # grabs 1st index to 4th index
print(a[0:]) # essentially grabs all
print(a[:3]) # print 0th index to 3rd 
print(a[-1]) # last element... like so on -2, -3
print(a[::2]) # like step size 2... 
print(a[::-2]) # from backwards
# intertingly, lets reverse a string
print(a[::-1]) # reversed!!! nice -- step (-1) backwards is a reverse right

#a[0]='x' || means its immutable, but you can change entire thinggy
a=a+' add me to end'
print(a)
print(a*3 ) # prints 3 times
a='hello white space yea'
b=5
print(a.split('e')) # return a list, where split happened on e
print(a.split(" ")) # splits on whitespaces
print(a,b,a) # printing multiple data types in the same line
floatingNum=1.216545
print('Trying to print floating value: %0.2f' %(floatingNum)) # printing with precision
print('lets try to print wiht specifier :%s: and yea its working' %(a))

x1 = 22.651
print(type(x1))
print(int(x1)) # casting int on float