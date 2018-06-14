#Pratice Python Problem 4
#Create a program that finds asks for a number and then finds the divisors
#variable = range(x,y) - creates a list of numbers between x and y, but
#                      - does not include y, only up to

number = int(input("Choose a number: "))

x = range(2, number + 1)

print("The divisors are ")

def findDivisors():
    for i in x:
        if number % i == 0:
            print(i)

findDivisors()
    
