#Cows and Bulls

import random

def main():
    print("Welcome to Cows and Bulls")
    random_number = generate()

    
    user_guess = str(input("Guess the 4 digit number\n--->"))
    algorithm(user_guess, random_number)

def algorithm(user_guess, random_number):
    #resetting counters
    cow  = 0
    bull = 0
    
    for i in range(0,4):
        if user_guess[i] == random_number[i]:
            cow += 1
        elif user_guess[i] in random_number:
            bull += 1
    print("You have {0} Cows and {1} Bulls".format(cow,bull))

def generate():
    return str(random.randrange(1000, 9999))

if __name__ == "__main__":
    main()
