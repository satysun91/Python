
class Pet:

    file_path = r"c:\wiseowl\pets\\"
    
    def __init__(self,name:str,animal:str,colour:str):

        self.name = name
        self.animal = animal
        self.colour = colour

# create 3 new pets
alfie = Pet("Alfie","Dog","Brown and white")
neo = Pet("Neo","Cat","Black and white")
annie = Pet("Annie","Cat","Tortoiseshell")

# Alfie has 4 legs
# alfie.legs = 4

# change the file path for Neo
# neo.file_path = r"c:\wiseowl\pets2\\"

# instance attributes created on the fly
# class attributes

# put pets in list and print
pets = [alfie,neo,annie]
for pet in pets:
    print(pet.name,pet.file_path)
