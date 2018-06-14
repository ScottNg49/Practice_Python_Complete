#Pratice Python Problem 5
#Write a program that returns a lsit that contains only the elements that are
#Common between the lists (without duplicates).
#import random

import random

print("Two lists will be randomly generated")
a = random.sample(range(30),10)
b = random.sample(range(30),10)
                        
print("List one contains ", a)
print("List two contains ", b)

print ([x for x in a if x in b],'are common integers between A and B')
