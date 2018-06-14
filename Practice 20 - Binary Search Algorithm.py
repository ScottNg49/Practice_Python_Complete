#Date 7/20/17
#Practice Python #20
#Create a binary search algorithm for an ordered list
#Binary search works by continually the midpoint(half) of the list
#And then uses recursion to return the correspoding other half

def binarySearch(aList, search):
    #First must check if the list has more than one value
    #Using <= rather than == as the argument len(aList) may skip 1
    #Error Prevention
    if len(aList) <= 1 and aList[0] != search:
        print("Number not found")
        
    #If the number is found, recursion will not continue
    elif search == aList[len(aList)//2]:
        print("The number has been found")
        
    #Returns the upperhalf of the list
    elif search > aList[len(aList)//2]:
        binarySearch(aList[len(aList)//2+1:],search)
        
    #Returns the lower half othe list
    elif search < aList[len(aList)//2]:
        binarySearch(aList[:len(aList)//2],search)

def main():
    aList = [1,3,5,30,42,43,500]
    binarySearch(aList, 2)

if __name__ == "__main__":
    main()
