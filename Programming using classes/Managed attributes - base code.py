
class Pet:

    file_path = r"c:\wiseowl\pets\\"
    
    def __init__(self,name:str,animal:str,colour:str):

        self.name = name
        self.animal = animal
        self.colour = colour

    def save(self,file_name:str):

        # open file for writing
        with open(self.file_path + file_name,"a") as pet_file:

            pet_file.write("{0},{1},{2}\n".format(self.name,self.animal,self.colour))

    # get clause for property
    # @property
    # def x(self):
    #     return self._x

    # # set clause for property
    # @x.setter
    # def x(self, value):
    #     self._x = value

    # # deleting the property (you probably won't need this bit)
    # @x.deleter
    # def x(self):
    #     del self._x

# create 3 new pets
alfie = Pet("Alfie","Dog","Brown and white")
neo = Pet("Neo","Cat","Black and white")
annie = Pet("Annie","Cat","Tortoiseshell")


