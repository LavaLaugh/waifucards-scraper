import re

f = open("cards.txt", "r")
content_lines = f.readlines()
content = f.read()

fd = open('cards.csv','a+')

name_pattern = r'alt="([^"]*)"|credittext="([^"]*)"'

number_pattern = r'/img/cards/(.*?).png'

def list_of_characters(content, name_pattern, fd):
    
    
    matches = re.findall(name_pattern, content)
    
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


def list_of_cards(content_lines, name_pattern, number_pattern):
    for i in content_lines:
        if "card-dropdown" in i:
            name_matches = re.findall(name_pattern, i)
            number_matches = re.findall(number_pattern, i)
            print(name_matches)
            print(number_matches)
            

list_of_cards(content_lines, name_pattern, number_pattern)
