
import json

# read in the file
with open(r"C:\__work\Python\tutorial\16c - JSON\sorting hat.json","r") as json_file:

    # load JSON data into variable
    potter_people = json.load(json_file)

# test this
for character in potter_people:

    # print first and last name
    print(" ".join(character[0:2]))