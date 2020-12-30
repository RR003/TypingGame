import levels
import random
fileObj = open("hackathon2020/words.txt", "r")  # opens the file in read mode
words = fileObj.read().splitlines()  # puts the file into an array
fileObj.close()


def mainProcess3(list, numOfWords):
    i = 0
    string2solve = ""
    while i < numOfWords:
        a = random.choice(list)
        listOfA = [letter for letter in a]
        listOfA[0] = listOfA[0].upper()
        s = ""
        b = s.join(listOfA)
        string2solve = string2solve + b + " "
        i = i + 1
    return string2solve


def TypeChallenge():
    global numOfWords
    numOfWords = 10
    string2solve = mainProcess3(words, numOfWords)
    return string2solve
TypeChallenge()

def wpm(elpasedTime, numOfWords):
    wpm = (numOfWords / elpasedTime) * 60
    return wpm
