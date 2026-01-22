
class Pet:
    
    file_path = r"c:\wiseowl\pets\\"
    
    def __init__(self,name:str,animal:str,colour:str):

        
        self.name = name
        self.animal = animal
        self.colour = colour
        self._ifrecorded = None

    def save(self,file_name:str):

        # open file for writing
        with open(self.file_path + file_name,"a") as pet_file:

            pet_file.write("{0},{1},{2}\n".format(self.name,self.animal,self.colour))

    # get clause for property
    @property
    def ifrecorded(self):

        # initialise the hidden attribute
        self._ifrecorded = False

        # does this pet exist in the text file
        with open(self.file_path + "pets.txt","r") as pet_file:
            for line in pet_file:
                if line.upper().startswith(self.name.upper() + ","):
                    self._ifrecorded = True
                    break
    
        return self._ifrecorded

    # set clause for property
    @ifrecorded.setter
    def ifrecorded(self, value):

        # if setting the value to be false, don't need to do anything
        self._ifrecorded = value

        if value == False:
            return

        # save this pet
        self.save("pets.txt")
        
    # deleting the property (you probably won't need this bit)
    # @x.deleter
    # def x(self):
    #     del self._x

    def __str__(self):
        return "{0} ({1} {2})".format(self.name,self.colour,self.animal)

# create 3 new pets
alfie = Pet("Alfie","Dog","Brown and white")
neo = Pet("Neo","Cat","Black and white")
annie = Pet("Annie","Cat","Tortoiseshell")

# list out pets
pets = [alfie,neo,annie]
for pet in pets:

    # if not already in text file, add this pet
    if not pet.ifrecorded:
        pet.ifrecorded = True


