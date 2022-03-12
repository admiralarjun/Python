from contextlib import redirect_stderr
from pickletools import read_unicodestring1


class Circle(object):
    pi = 3.14
    color = 'red'

    def __init__(self,rad): # initiate all attributes
        self.radius = rad

    def area(self):
        res = (self.radius**2)*Circle.pi
        return res
    def circumference(self):
        return 2*self.pi*self.radius

    def set_rad(self,newRad):
        self.radius = newRad
    def get_rad(self):
        return self.radius        

# create a circle with radius
c1 = Circle(rad=10)
print(c1.radius)
c1.set_rad(20)
print(c1.radius)
# or we can use getter thingy
print("From getter",c1.get_rad())
print("Circumference of the circle is: %.2f" %(c1.circumference()))
