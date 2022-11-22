secretWord = "PROFESSOR"
copy = secretWord
guessedLetters =[]
wordBoard = ["_"]*len(secretWord)
turns = 5
#Create a function called “showBoard” that will display the current board state which is stored in the variable “wordBoard”
def showBoard():
    print(" ".join(wordBoard))

def checkGuess(guessed,secretWord,wordBoard):
    index = secretWord.find(guessed)
    while index != -1:
        if guessed in secretWord:
            index = secretWord.find(guessed)
            remove = "*"
            secretWord = secretWord[:index]+ remove + secretWord[index+1:]
            wordBoard[index] = guessed
        else:
            index = -1
    return(secretWord,wordBoard)

def win():
    for x in range(0,len(wordBoard)):
        if wordBoard[x] == "_":
            return -1
    return 1

print("Can you guess the secret occupation? ")


while(turns):
    showBoard()
    userInput = input("Guess a letter: ").upper()
    if userInput in secretWord:
        secretWord,wordBoard = checkGuess(userInput,secretWord,wordBoard)
        guessedLetters.append(userInput)
    elif userInput in secretWord:
        print("you already guessed "+ userInput)
        turns = turns
    else:
        print("That letter is not a part of this word.")
        turns = turns -1
        guessedLetters.append(userInput)
    if win() == 1:
        turns = 0
        print("YOU WON "+ copy)
    elif turns == 0:
        print("Sorry you lost")

    print("you have " + str(turns)+ " turns left")
    print()



