
class Pet:

    file_path = r"c:\wiseowl\pets\\"
    
    def __init__(self,name:str=None,animal:str=None,colour:str=None):

        self.name = name
        self.animal = animal
        self.colour = colour

    @classmethod
    def from_line(cls,line_of_text:str):

        # create a new pet object from this line of text
        nam, anima, colou = line_of_text.split(",")

        this_pet = cls(nam,anima,colou)
        return this_pet

    def save(self,file_name:str):

        # open file for writing
        with open(self.file_path + file_name,"a") as pet_file:

            pet_file.write("{0},{1},{2}\n".format(self.name,self.animal,self.colour))

# create 3 new pets
# alfie = Pet("Alfie","Dog","Brown and white")
# neo = Pet("Neo","Cat","Black and white")
# annie = Pet("Annie","Cat","Tortoiseshell")

# # put pets in list and print
# pets = [alfie,neo,annie]
# for pet in pets:
#     pet.save("pets.txt")

pets = []
with open(r"c:\wiseowl\pets\pets.txt","r") as pet_file:

    # read in all but first line
    lines = pet_file.read().splitlines()[1:]

    # create pet from each line
    for line in lines:

        # create a new pet and add it to list
        new_pet = Pet.from_line(line)
        pets.append(new_pet)

# list out pets
for pet in pets:
    print(pet.name,pet.animal,pet.colour)
