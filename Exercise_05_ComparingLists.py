#Take two lists, and write a program that returns a list that contains only the elements that are common
# between the lists (without duplicates). Make sure your program works on two lists of different sizes.

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] #this is an example list
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] #this is an example list
n_a = int(input("Give a size of first list: "))
n_b = int(input("Give a size of second list: "))
a = list()
b = list()
c = list()

import random
for i in range (n_a):
    a.append(random.randint(0,30))

for i in range (n_b):
    b.append(random.randint(0,30))

print("List A: ", a)
print("List B: ", b)

for i in range(0,n_a):
    for j in range(0,n_b):
        if a[i] == b[j]:
            c.append(a[i])

print("Duplcates are: ", list(dict.fromkeys(c)))
