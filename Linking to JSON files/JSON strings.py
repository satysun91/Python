
import json

potter_list = (
	("Hermione","Granger","Gryffindor",4),
	("Draco","Malfoy","Slytherin",7),
	("Harry","Potter","Gryffindor",6),
)

# write to a string variable
characters = json.dumps(potter_list)

# read back in
potter_characters = json.loads(characters)

print(type(potter_characters))
print(potter_characters)