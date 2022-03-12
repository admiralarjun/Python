# class

class Dog(object):

    # class obejct attribute
    species = 'Mammal'
    # regardless of what breed the dog is, its mammal

    def __init__(self,breed): # initialize the attribute
        self.breed = breed # self refers to Dog here.
       # Dog.breed = breed # this will also work

    

sam = Dog(breed='Beagle')
print(sam.breed,"is a",sam.species)
 