#Write a program that takes the beginning element and a end element fo a list
#A list will be predefined

def stagger(lists):
    newList = (lists[0], lists[-1])
    return newList
    
x = [5, 10, 15, 20, 25]

x = stagger(x)
print(x)
