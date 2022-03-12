# inheritance

class Animal(object): # base class
    def __init__(self):
        print("This is animal class speaking")
    def eat(self):
        print("Eating") 
    def speak(self):
        print("I can't speak you dum")      

# derived class
class Dog(Animal): # instead of object, we are passing the another class for inheriting
    def __init__(self):
        Animal.__init__(self)
    def bark(self):
        print("Woof!")
    def whoami(self):
        print("I am dog")    

d = Dog() # creating a instance d

print(d.speak())

# even though the Dog class don't have speak method,
# since it is inherited from Animal class, the sepak() still works!
