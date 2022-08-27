#Learning Python!
from math import*


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
    print(str(0) + " is my favorite number") #converts 5 to str
    n = -1
    print(abs(n)) #absolute value of n  
    print(pow(3,2)) #3^2
    print(max(1,5)) ,  print(min(1,5)) #finds max and min
    print(round(3.6)) #round num up or down
    print(floor(3.5)) , print(ceil(3.5)) #takes away decimal, and always rounds up    
    print(sqrt(36)) #square root

def myInput():
    name = input("Enter name: ")
    print("Length of your name is: " + len(name))
