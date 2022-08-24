#Learning Python!

def smileyFace():
    print("[]   []")
    print("  /_   ")
    print("       ")
    print("|_____|")

def datatypevar():
    charAge = "21" #this is a string
    charName = "Michael"
    print("My name is " + charName +" and I am " + charAge + " years old.")   

def strings():
    cat = "charlie"
    print(cat + " is cool")
    print(cat.upper())
    print(cat.upper().isupper()) #true or false if string is uppercase
    print(len(cat)) #length of str
    print(cat[0]) #prints first index
    print(cat.index("a")) #letter a is at index 2
    print(cat.replace("lie","les")) #replaces specified letters

def numbers():
    a = 1
    print(a)