original_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

new_list = []

number = int(input("Choose a number between 0 and 50: "))

def createNewList():
    for element in original_list:
        if element < number:
            new_list.append(element)

createNewList()
print(new_list)
