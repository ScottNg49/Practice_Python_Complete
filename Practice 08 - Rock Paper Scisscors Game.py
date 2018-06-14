#Create a Rock Paper Scisscors game with multiplayer and AI

import getpass
import random

def constructor():
    global leaveGame
    leaveGame = False

def openMenu():
    print("\nRo-sham-bo!\n"
          "1)Play against AI\n"
          "2)Play against a friend\n"
          "3)Quit the game\n")
    playType = str(input("Choose an option\n---> "))

    if playType == "1" or playType.lower() == "computer" or playType.lower() == "ai":
        AI()
        
    elif playType == "2" or playType.lower() == "multiplayer" or playType.lower() == "friend":
        multiplayer()

    elif playType == "3" or playType.lower() == "quit":
        global leaveGame
        leaveGame = True

    else:
        print("Please choose a valid option")
        openMenu()

def AI():
    allowed = ["rock", "paper", "scisscors", "Rock", "Paper", "Scisscors"]
    while leaveGame == False:
        computer = random.choice(allowed)
        player1 = input("Player 1, What is your action\n---> ")
        if player1 not in allowed:
            print ("Invalid Option! Try again!")
            continue
        
        else:
            if player1.lower() == computer.lower():
                print("Its a draw!\n")

            elif player1.lower() == "rock" and computer.lower() == "paper":
                print("The Computer has won!\n")

            elif player1.lower() == "paper" and computer.lower() == "scisscors":
                print("The Computer has won!\n")

            elif player1.lower() == "scisscors" and computer.lower() == "rock":
                print("The Computer has won!\n")

            #concludes that there is no way player 2 could of won, so player 1 wins
            else:
                print("Player1 has won!\n")

            print("Player1 has chosen", player1.lower(), "\nComputer has chosen", computer.lower())
            openMenu()
            
def multiplayer():
    print("\nRock, Papers, or Scissors!")
    #valid user input
    allowed = ["rock", "paper", "scisscors", "Rock", "Paper", "Scisscors"]
    while leaveGame == False:
        player1 = getpass.getpass(prompt="Player 1, What is your action\n--> ", stream=None)
        if player1 not in allowed:
            print ("Invalid Option! Try again!")
            continue
        player2 = getpass.getpass(prompt="Player 2, What is your action\n--> ", stream=None)
        if player2 not in allowed:
            print ("Invalid Option! Try Again!")
            continue

        else:
            if player1.lower() == player2.lower():
                print("Its a draw!\n")

            elif player1.lower() == "rock" and player2.lower() == "paper":
                print("Player2 has won!\n")

            elif player1.lower() == "paper" and player2.lower() == "scisscors":
                print("Player2 has won!\n")

            elif player1.lower() == "scisscors" and player2.lower() == "rock":
                print("Player2 has won!\n")

            #concludes that there is no way player 2 could of won, so player 1 wins
            else:
                print("Player1 has won!\n")

            print("Player1 has chosen", player1.lower(), "\nPlayer2 has chosen", player2.lower())
            openMenu()
            


#######################################################################

constructor()

while leaveGame == False:
    openMenu()
    
else:
    print("You have exited")
