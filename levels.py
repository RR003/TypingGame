import random

def randomSpaces():
    numberOfspaces = random.randint(1, 12)
    return numberOfspaces
randomSpaces()

def ElapsedTime(end, start):
    totalTime = end - start
    return totalTime

def limits(index):
    index = index - 1;
    limits = [120,120,120,120,120,120,120,120]
    return limits[index]

def checkAdvancement(elapsedTime, limit):
    if (elapsedTime <= limit):
        print("Congrats, you passed!!")
        return True
    else:
        print("You suck lol")
        return False

def mainProcess1(list, numOfLetters):
    i = 0
    spaces = randomSpaces()
    string2solve = ""
    while i < numOfLetters:
        if (spaces == 0):
            string2solve = string2solve + " "
            spaces = randomSpaces()
            a = random.choice(list)
            string2solve = string2solve + a
            spaces = spaces - 1
        else:
            spaces = spaces - 1
            a = random.choice(list)
            string2solve = string2solve + a
        i = i + 1
    return string2solve

def mainProcess2(lowerCase, upperCase, numOfLetters):
    i = 0
    spaces = randomSpaces()
    string2solve = ""
    while i < numOfLetters:
        if i == 0:
            a = random.choice(upperCase)
            string2solve = string2solve + a
            spaces = spaces - 1
        elif (spaces == 0):
            string2solve = string2solve + " "
            spaces = randomSpaces()
            a = random.choice(upperCase)
            string2solve = string2solve + a
            spaces = spaces - 1
        else:
            spaces = spaces - 1
            a = random.choice(lowerCase)
            string2solve = string2solve + a
        i = i + 1
    return string2solve

def level1():
    possibleLetters = ['a','s','d','f','g','h','j','k',";"];
    numOfLetters = 120
    time = 100
    string2solve = mainProcess1(possibleLetters, numOfLetters)
    return string2solve, time


def level2():
    possibleLetters = ['a','s','d','f','g','h','j','k', "r","e","u","i"]
    numOfLetters = 140
    time = 95
    string2solve = mainProcess1(possibleLetters, numOfLetters)
    return string2solve, time


def level3():
    possibleLetters = ['a','s','d','f','g','h','j','k', "r","e","u","i"
                       'q', 'w', 'o', 'p']
    numOfLetters = 150
    time = 90
    string2solve = mainProcess1(possibleLetters, numOfLetters)
    return string2solve, time

def level4():
    possibleLetters = ['a','s','d','f','g','h','j','k', "r","e","u","i"
                       'q', 'w', 'o', 'p', 'c', 'v', 'b', 'n']
    numOfLetters = 155
    time = 85
    string2solve = mainProcess1(possibleLetters, numOfLetters)
    return string2solve, time

def level5():
    possibleLetters = ['a','s','d','f','g','h','j','k',"r","e","u","i"
                       'q', 'w', 'o', 'p', 'c', 'v', 'b', 'n', 'z', 'x','m']
    numOfLetters = 160
    time = 80
    string2solve = mainProcess1(possibleLetters, numOfLetters)
    return string2solve, time

def level6():
    lowerLetters = ['a','s','d','f','g','h','j','k',"r","e","u","i"
                       'q', 'w', 'o', 'p', 'c', 'v', 'b', 'n', 'z', 'x','m']
    upperCase = ['A','S','D','F', 'G','H','J','K','L']
    numOfLetters = 170
    time = 80
    string2solve = mainProcess2(lowerLetters, upperCase, numOfLetters)
    return string2solve, time

def level7():
    time = 90
    lowerLetters = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', "r", "e", "u", "i"                                                    
                        'q', 'w', 'o', 'p', 'c', 'v', 'b', 'n',
                       'z', 'x', 'm']
    upperCase = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Q','W','E','R','T',
                 'Y','U','I','O','P']
    numOfLetters = 180
    string2solve = mainProcess2(lowerLetters, upperCase, numOfLetters)
    return string2solve, time

def level8():
    time = 85
    lowerLetters = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', "r", "e", "u", "i"
                                                                           'q', 'w', 'o', 'p', 'c', 'v', 'b', 'n',
                    'z', 'x', 'm']
    upperCase = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Q', 'W', 'E', 'R', 'T',
                 'Y', 'U', 'I', 'O', 'P', 'Z','X','C','V','B','N','M']
    numOfLetters = 200
    string2solve = mainProcess2(lowerLetters, upperCase, numOfLetters)
    return string2solve, time

