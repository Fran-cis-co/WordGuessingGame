# Python file which begins the guessing game
import database.words as words
import utility.randomWordFromArray as randomize

def startTheGuessing():
    # Variable which calls the database file, then calls the utility file which picks a random word from the database
    randomWord = randomize.getRandomWord(words.getWords())
    numOfGuesses = len(randomWord) + 2 # Number of guesses = length of word + 2

def beginGame():
    # Keep in while loop to keep the game going until user decides to quit
    while(True):
        # Ask the user for input whether to play the game or quit it
        playGame = input("Hello, enter 1 to begin the game or 2 to quit: ")

        '''
            Use match case statement to determine whether to start the game or quit the program.
            We use quotations instead of an integer in the cases since the input() function interprets the user input as a string.
        '''
        match playGame:
            case "1":
                startTheGuessing()
            case "2":
                print("quit the game")
                break
            case _:
                print("You did not input something correct.")
    # print(randomize.getRandomWord(database))
