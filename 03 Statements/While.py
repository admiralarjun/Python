''' Basic form
while test:
    code statement
else:
    another code  statement  
'''
x = 1
table = int(input("Enter which table to print: "))
while x <= 10:
    print(table,"X",x,"=",table*x)
    x += 1
else:
    print("----END----")


