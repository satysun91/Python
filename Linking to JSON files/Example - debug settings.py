
import json

# read in JSON debug settings file
with open(r"C:\__work\Python\tutorial\16c - JSON\launch.json") as settings_file:

    # load this into variable
    settings = json.load(settings_file)

# test this
configurations = settings["configurations"]

real_config = configurations[0]

jmc = real_config["justMyCode"]

print(jmc)