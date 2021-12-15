import re

logfile = input("Enter full path to log file:")
if ".txt" not in logfile:
    logfile = logfile + ".txt"

with open(logfile, "r") as f:
    file = f.read()

matches = re.findall("--------------------------------------[A-z\s0-9:-]+-----------------------------------------------", file)

recipes = []
for match in matches:
    formatted_match = re.sub("\[[A-z\s0-9:]+\] ", "", match)
    formatted_match = re.sub("-", "", formatted_match)
    recipes.append(formatted_match)


with open("Recipes.txt", "w") as f:
    f.write("".join(recipes))
