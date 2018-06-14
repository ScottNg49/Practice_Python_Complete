#Practice Python 6
#Asks a user for a string and then reverses the string
#Function will then check if the string is palindrome
#Ex: Eye = True, Hello = False, Racecar = True

print("Palindrome Checker")
string = input("Choose a word: ")

#converting to all lower case in case of capitalization
string = string.lower()

#reverses the string
rString = string[::-1]

if string == rString:
    print("This is a Palindrome")
else:
    print("This is not a Palindrome")

print("The original word is ",string)
print("The reversed word is ",rString)

