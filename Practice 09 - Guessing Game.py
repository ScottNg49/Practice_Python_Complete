#Date ??/??/2017
#create a guessing game
#count the number of correct and total guesses

import random, time, os

def main():
    #pastGuess = past user guesses
    #noGuess   = number of guesses
    print("\nWelcome to the guessing game."
          "\nGuess the number between 1 and 100.")
    guess        = int(input("What do you think the number is?\n--->"))
    pastGuess    = []
    noGuess      = 1
    randomNumber = random.randint(1,100)

    #Calling the guessingGame function
    guessingGame(guess, pastGuess, noGuess, randomNumber)
        
def guessingGame(guess, pastGuess, noGuess, randomNumber):

    #While loop continues until the number is found
    while guess != randomNumber:
        if guess in pastGuess:
            print("You have already chosen this number!",
                  "\nThe numbers you have chosen are", pastGuess)
            guess = int(input("What do you think the number is?\n-->"))
            noGuess +=1
        
        elif guess > randomNumber:
           pastGuess.append(guess)
           pastGuess = sorted(pastGuess)
           print("\nThe number is smaller than", guess, "!")
           print("You have chosen the numbers", pastGuess)
           guess = int(input("What do you think the number is?\n--->"))
           noGuess += 1
       
        elif guess < randomNumber:
            pastGuess.append(guess)
            pastGuess = sorted(pastGuess)
            print("\nThe number is larger than", guess, "!")
            print("You have chosen the numbers", pastGuess)
            guess = int(input("What do you think the number is?\n--->"))
            noGuess += 1

    print("Congratulations, You have found the number!\n"
          "It is", guess,
          "It took you a total of", noGuess, "tries")
    time.sleep(5)

        
if __name__ == "__main__":
    main()
