#Create a prime number checker with functions

import math
import time

def getNumber():
    return int(input("What number would you like to check: "))

#Checks up until half of numbers
def isPrime(number):
    for x in range(2,math.ceil(number/2)):
        if number % x == 0:
            return False
    return True

number = getNumber()

if isPrime(number) and number != 1:
    print("The number is prime")
else:
    print("The number is not prime")
time.sleep(2)



    
