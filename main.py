import database.words as words
import utility.randomWordFromArray as randomize

# Variable to store the database to use in the main file
database = words.getWords()

print(randomize.getRandomWord(database))