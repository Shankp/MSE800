import random

def GenerateRandomWord():
    words = ["test", "example", "python", "code", "random"]
    print("Generating a random word...")   
    randomWord = random.choice(words)
    print("Random word length:", len(randomWord))
    return randomWord

def GenerateBlanksInRandomWord(randomWord):
    print("Generating blanks in the random word...")
    randdomNumber = random.randint(0, len(randomWord) - 1)
    blanks = randomWord.replace(randomWord[randdomNumber], "_")
    return blanks

def CheckUserInput(randowmword, randomWordWithBlank, userInputLetter):
    numberOfTries = 5
    while numberOfTries >= 0:            
        blankIndex = randomWordWithBlank.find("_")   
        alist = list(randomWordWithBlank)
        alist[blankIndex] = userInputLetter
        randomWordWithBlank =   ''.join(alist)

        if randowmword == randomWordWithBlank:
            print("Congratulations! You guessed the word correctly.")
            break
        else:           
            print("Sorry, that's not correct. Try again!")
            numberOfTries -= 1
            if(numberOfTries == 0):
                print("You have no more tries left.")
                return False
            else:
                print(f"You have {numberOfTries} tries left.")
                userInputLetter = input("Enter another guess: ")
   
    if(numberOfTries == -1):
        print("Game over! You've used all your tries.")
        return False



if __name__ == "__main__":
    print("Welcome to the Word Game!")
    randowmword = GenerateRandomWord()

    blanks = GenerateBlanksInRandomWord(randowmword)
    userInput = input("Enter your guess: ")

    gameStatus = CheckUserInput(randowmword, blanks, userInput)
    if gameStatus is not False:
        print("You guessed the word successfully!")   
    print("Thank you for playing the word game!")
