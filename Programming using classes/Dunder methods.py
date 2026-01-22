class Pet:

    """
        This holds details of each pet
        Written by Sven
    """
    
    def __init__(self,name:str,animal:str,colour:str):

        self.name = name
        self.animal = animal
        self.colour = colour

    def __str__(self):

        # return readable text for this object
        return "{0} is a {1} {2}".format(self.name,self.colour,self.animal)

# create 3 new pets
alfie = Pet("Alfie","Dog","Brown and white")
neo = Pet("Neo","Cat","Black and white")
annie = Pet("Annie","Cat","Tortoiseshell")

# put pets in list and print
pets = [alfie,neo,annie]
for pet in pets:
    print(pet.name)

# print documentation for class
print(annie)
