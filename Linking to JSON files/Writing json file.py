
potter_list = (
	("Hermione","Granger","Gryffindor",4),
	("Draco","Malfoy","Slytherin",7),
	("Harry","Potter","Gryffindor",6),
)

import json

with open(r"C:\__work\Python\tutorial\16c - JSON\sorting hat.json","w") as json_file:

    # dump the Harry Potter info
    json.dump(potter_list,fp=json_file,indent=4)

    