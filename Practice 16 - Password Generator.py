#Date ??/??/2017
#Practice Python #16 - Password Generator
#Ask the user how strong they want their password to be
#For a weak password, pick a word or two from a list


import random
import time

def main():
    choice = menu()
    password = generatePassword(choice)
    print("Your password is",password) 

def menu():
    choice = input("Do you want a weak or strong password:\n---> ")
    return choice

def generatePassword(choice):
    if choice.lower() == "weak" or choice.lower() == "w":
        print("You have chosen a weak password")
        password = random.choice(['Scott', 'April', 'Bryan', 'Grace']) + random.choice(['Scott','April','Bryan','Grace'])
    elif choice.lower() == "strong" or choice.lower() == "s":
        print("You have chosen a strong password")
        keywords = "!@#$%^&*()qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASFGHJKLZXCVBNM"
        password = ''.join(map(str,random.sample(keywords, 10)))
    else:
        print("Choose a valid option")
    return password

if __name__ == "__main__":
    main()
           
