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

def calculate():
    num1 = input("Enter number: ") #input is always read as str 
    num2 = input("Enter second number: ")
    result = int(num1) + int(num2) #int turns input to int
    print(result)
    
def myList():
    friends = ["bob","jim","kim"]
    print(friends[0]) #prints first element in list

def listfnx():
    luckyNums = [7,11,13,0,5]
    friends = ["bob","jim","kim"]
    friends.extend(luckyNums) #adds luckynums to back of list
    friends.append("Mike") #adds 1 element to list
    friends.insert(1, "kelly") #inserts at index 
    friends.remove("jim") #jim is removed
    friends.pop() #remove last element from list
    print(friends.index("bob")) #prints index of element
    print(friends.count("bob")) #counts how many bobs in list
    luckyNums.sort() #sorts luckynum list
    friends2 = friends.copy() #copies list
    print(friends)

def tuples():
    coordinates = (3, 5)
    print(coordinates[0])