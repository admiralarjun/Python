'''
def testFunction(a,b):
    print(a+b)

testFunction(5,6)
'''
import math

def isPrime(n):
    flag = 0
    for i in range(2,math.isqrt(n)):    # optimized way
    #for i in range(2,int(n/2)):        # less optimized
    #for i in range(2,int(n)):          # no optimization lol     
        if(n%i==0):
            flag = 1
    if(flag == 1):
        return 'Not a prime'
    else:
        return 'prime' 

n = int(input("Enter num to check prime or not: "))
print("The given number {0} is".format(n),isPrime(n))        

''' string formatting is performed in above print
{0} indicates the .format(n) position (0 - n)
it can be like - "{0} said hi to {1}".format(ram,raj)
{0} - ram, {1} - raj
'''