import random

class RandomwordGenerator:
    def generate_randomWord(self):
        words = ["test", "example", "python", "code", "random"]
        print("Generating a random word...")   
        randomWord = random.choice(words)
        print("Random word length:", len(randomWord))
        return randomWord

    def generate_blanks(self, randomWord):
        print("Generating blanks in the random word...")
        randdomNumber = random.randint(0, len(randomWord) - 1)
        blanks = randomWord.replace(randomWord[randdomNumber], "_")
        return blanks
    
class Wordgame:
    def  __init__(self, word, blanked_word, user_input_letter ):
        self.randowmword = word
        self.randomWordWithBlank = blanked_word
        self.userInputLetter = user_input_letter


    def play(self):
        numberOfTries = 5
        while numberOfTries >= 0:            
            blankIndex = self.randomWordWithBlank.find("_")   
            alist = list(self.randomWordWithBlank)
            alist[blankIndex] = self.userInputLetter
            self.randomWordWithBlank =   ''.join(alist)

            if randowmword == self.randomWordWithBlank:
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
                    self.userInputLetter = input("Enter another guess: ")
   
        if(numberOfTries == -1):
            print("Game over! You've used all your tries.")
            return False



if __name__ == "__main__":
    print("Welcome to the Word Game!")
    rand_word_generator = RandomwordGenerator()
    randowmword = rand_word_generator.generate_randomWord()
    blanks = rand_word_generator.generate_blanks(randowmword)
  
    userInput = input("Enter your guess: ")

    word_game = Wordgame(randowmword, blanks, userInput)
    game_status = word_game.play()
    if game_status is not False:
        print("You guessed the word successfully!")   
    print("Thank you for playing the word game!")
