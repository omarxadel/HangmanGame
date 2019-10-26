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
            print(counter)
            return True
        counter = counter + 1
    return False

def engine():
    gameWord = randomWordGenerator(randomNumberGenerator())
    userIn = getConsoleInput()
    print(letterInWord(userIn, gameWord))

engine()

