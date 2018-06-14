#Write one of Python that takes this list and makes a new list
# that has only the even elements of this list in it

#predefined list
#can also use [y**2 for y in range(1,11)]
a = [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = ([x for x in a if x % 2 == 0])

print(b)

#one line code
#print(x for x in [y**2 for y in range(1,11) if x % 2 == 0)
