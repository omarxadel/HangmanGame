import pandas as pd
import numpy as np
import csv

#Load Words in a Dictionary
reader_count = 0
words_dict = {}

with open('words.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        words_dict[reader_count] = row[0]
        reader_count = reader_count + 1
csvFile.close()

#Create Number Generator
def randomNumberGenerator():
    return np.random.randint(0,5)

#Random Word Generator
def randomWordGenerator(num):
    random_word = words_dict[num]
    return random_word

#Console Input Tester
def getConsoleInput():
    user_input = input("Enter a letter: ")
    return user_input

#Game Engine
def letterInWord(letter, word):
    counter = 0
    while(counter<len(word)):
        if(letter != word[counter]):
            counter += 1
            continue
        else:
            return True
        counter = counter + 1
    return False

def wordToLetters(word):
    counter = 0
    letters = []
    while(counter<len(word)):
        if word[counter] not in letters:
            letters.append(word[counter])
        counter += 1
    return letters

def printWelcome(word):
    print("Your word is: ", end="")
    counter = 0
    while(counter < len(word)-1):
        print("_ ",end="")
        counter += 1
    print("_")

def printGuessed(guessed, word):
    counter = 0
    while(counter < len(word)):
        if(word[counter] in guessed):
            print(word[counter], end= "")
        else:
            print("_ ", end= "")
        counter += 1

def engine():
    lives = 6
    gameWord = randomWordGenerator(randomNumberGenerator())
    gameWordLetters = sorted(wordToLetters(gameWord))
    inLetters = []
    printWelcome(gameWord)
    while(lives >= 0):
        
        userIn = getConsoleInput()
        if(letterInWord(userIn, gameWord) and inLetters.count(userIn) == 0):
            inLetters.append(userIn)
            print("Good Job!, Guess another one!")
        elif(inLetters.count(userIn) > 0):
            print("Already guessed it!")
        else:
            lives -= 1
            print("Unfortunate! You Got " + str(lives) + " Lives Only!")
        
        printGuessed(inLetters, gameWord)
        inLetters = sorted(inLetters)
        if(inLetters == gameWordLetters):
            print("YOU WON!")
            break
        

engine()

