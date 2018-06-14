#Date ??/??/2017
#Practice Python #13 - Fibonacci
#Create fibonnaci's sequence

import time

def fibonacci(number):
    aList = [1,1]
    listRange = range(2,number)
    for x in listRange:
        a = aList[-2] + aList[-1]
        aList.append(a)
    print(aList)
    
def chooseNumber():
    return int(input("Choose an ending point: "))

def main():
    number = chooseNumber()
    fibonacci(number)
    time.sleep(5)

if __name__ == "__main__":
    main()
