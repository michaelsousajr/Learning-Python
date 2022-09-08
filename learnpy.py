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
    
def myReturn(num):
    result =  num * num * num
    print(result)
    return result

def myIf():
    isMale = True
    if isMale:
        print("you are male")
    else: 
        print("You are not a male")
        
def maxNum(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(str(num1)+" is the biggest num")
    elif num2 > num1 and num2 > num3:
        print(str(num2)+" is the biggest num")
    elif num1 == num2 and num2 == num3:
        print("all numbers are the same")
    else:
        print(str(num3)+" is the biggest num")

def calculatorPlus():
    userNum1 = float(input("Enter first num: "))
    userOp = input("Enter operator: ")
    userNum2 = float(input("Enter second num: "))
    
    
    if userOp == "+":
        print(userNum1+userNum2)
    elif userOp == "-":
        print(userNum1-userNum2)
    elif userOp == "/":
        print(userNum1/userNum2)
    elif userOp == "*":
        print(userNum1*userNum2)
    else:
        print("Invalid input")

def converter():
    monthCon = {
        "Jan" : "January",
        "Feb" : "Febuary",
        "Mar" : "March",
    }
    numCon = {
        1 : "One",
        2 : "Two",
        3 : "Three"
    }
    print(monthCon["Mar"])
    print(numCon[1])

def whileLoop():
    a = 0
    while a < 10:
        print(a)
        a += 1
        
def guessingGame():
    secretWord = "secret"
    guess = ""
    guessCount = 0
    guessLimit = 3
    guessBool = False

    while guess != secretWord and not(guessBool):
        if guessCount < guessLimit:
            guess = input("Enter guess: ")
            guessCount += 1
        else:
            guessBool = True

    if guessBool:
        print("You Lose")
    else:
        print("You Win")
        
def forLoops():
    for letter in "Michael Sousa":
        print(letter, end = "")
    
    friends = ["mike", "jim", "bob"]
    for friend in friends:
        print (friend)
        
    for index in range(10):
        print(index)    

    for index in range(1,3):
        print(index)
    
    for index in range(5):
        if index == 0:
            print("first interation")
        else:
            print("not first")

def exponents(baseNum,pow):
        print(baseNum**pow)
        
def grid():
    myGrid = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [0]
    ]
    
    print(myGrid[0][0])
    
    for row in myGrid:
        for col in row:
            print(col)


def translate():
    phrase = input("Enter Phrase: ")
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":

            if letter.isupper():
                translation = translation + "G"

            else:
                translation = translation + "g"

        else:
            translation = translation + letter       

    print(translation)

def comment():
    '''
    this is
    my comment
    '''
    
    #this is my other comment
    
    print("this line works")
    
def tryExcept():
    try:
        answer = 10/0
        number = int(input("Enter a number: "))
        print(number)
    except ZeroDivisionError as err: 
        print(err)
    except ValueError:
        print("invalid input")
