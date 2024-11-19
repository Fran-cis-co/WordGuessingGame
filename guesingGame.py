# Python file which begins the guessing game
import database.words as words
import utility.randomWordFromArray as randomize

# Function to determine if the game should end or not depending on the amount of guesses the user has left
def checkGuesses(numOfGuesses):
    if numOfGuesses == 0:
        print("You ran out of tries! Exiting game.")
        return True
    else:
        return False       

def startTheGuessing():
    # Variable which calls the database file, then calls the utility file which picks a random word from the database
    randomWord = randomize.getRandomWord(words.getWords())
    numOfGuesses = len(randomWord) + 2 # Number of guesses = length of word + 2

    # Let player know how many letters their word has
    print("Your word is", numOfGuesses, "letters long.")

    # We put the game in a while loop that way we can have the player always inputting their guesses
    while(True):
        print("You have", numOfGuesses, "left \n")
        # One of the ways the game will end is if the user runs out of guesses   
        if checkGuesses(numOfGuesses):
            break
        

        # Grab the input from the user and then determine if it is a correct guess
        characterGuess = input("Please Input your guess: ")
        if characterGuess.isdigit():
            print("Input must be a character")
            continue
    
def beginGame():
    # Keep in while loop to keep the game going until user decides to quit
    while(True):
        # Ask the user for input whether to play the game or quit it
        playGame = input("Hello, enter 1 to begin the game or 2 to quit: \n")

        '''
            Use match case statement to determine whether to start the game or quit the program.
            We use quotations instead of an integer in the cases since the input() function interprets the user input as a string.
        '''
        match playGame:
            case "1":
                startTheGuessing()
            case "2":
                print("Thank you for playing!")
                break
            case _:
                print("You did not put the correct inputs. Please try again.")
    # print(randomize.getRandomWord(database))
