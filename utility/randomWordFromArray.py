'''
Utility file which is used to get a random word from the word database

This file uses the random library to randomly choose from the array database
'''
import random

def getRandomWord(list):
    return random.choice(list)