import re

f = open("cards.txt", "r")
content = f.read()

fd = open('cards.csv','a+')

pattern = r'alt="([^"]*)"|credittext="([^"]*)"'

matches = re.findall(pattern, content)

results = [match[0] if match[0] else match[1] for match in matches]

control = 0
writestring = ""
controlstring = ""
# Print the results
for result in results:
    if control == 1:
        writestring += result + "\n"
        #fd.write(result + "\n")
        control = 0

    elif control == 0:
        writestring += result + "|"
        #fd.write(result + ",")
        control = 1

    if writestring[-1] != "|":
        if writestring in controlstring:
            writestring = ""

        elif writestring not in controlstring:
            fd.write(writestring)
            controlstring += writestring
            writestring = ""


    print(result)
