import random

def GenerateRandomWord():
    words = ["test", "example", "python", "code", "random"]
    print("Generating a random word...")
    randomWord = random.choice(words)
    return randomWord

def GenerateBlanksInRandomWord(randomWord):
    print("Generating blanks in the random word...")
    randdomNumber = random.randint(0, len(randomWord) - 1)
    blanks = randomWord.replace(randomWord[randdomNumber], "_")
    return blanks

def CheckUserInput(randowmword, randomWordWithBlank, userInputLetter):
    numberOfTries = 5
    while numberOfTries > 0:  
          
        blankIndex = randomWordWithBlank.find("_")   
        alist = list(randomWordWithBlank)
        alist[blankIndex] = userInputLetter
        randomWordWithBlank =   ''.join(alist)
        numberOfTries -= 1

        if randowmword == randomWordWithBlank:
            print("Congratulations! You guessed the word correctly.")
            return
        else:           
            print("Sorry, that's not correct. Try again!")
            numberOfTries -= 1
            userInputLetter = input("Enter your guess: ")
   
    if(numberOfTries == -1):
        print("Game over! You've used all your tries.")
        return False



if __name__ == "__main__":
    randowmword = GenerateRandomWord()

    blanks = GenerateBlanksInRandomWord(randowmword)
    userInput = input("Enter your guess: ")

    gameStatus = CheckUserInput(randowmword, blanks, userInput)
    if gameStatus is not False:
        print("You guessed the word successfully!")   
    print("Thank you for playing the word game!")
