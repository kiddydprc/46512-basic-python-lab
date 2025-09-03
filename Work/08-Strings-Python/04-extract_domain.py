e = input()
pos = e.find('@') #find the position of '@'

if pos != -1:
    pos += 1
    atc = ""
    while pos < len(e) and e[pos] != " ": #until end of string
        atc += e[pos] #add to domain
        pos += 1
    print(atc)#print domain
else:
    print("") #no '@' found, print empty string


