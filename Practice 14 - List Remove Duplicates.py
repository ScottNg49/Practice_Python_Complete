#Exercise 14 - List Remove Duplicates
#Use set to covert list into a set
#A set does not have duplicates

def listReg():
    element = str(input("What would you like to add into the list? "))
    return element

mainList = ["Scott", "April", "Bryan", "Grace", "Scott"]
print("The current list is", mainList)

mainList = set(mainList)
print("Now, the list is", mainList)
