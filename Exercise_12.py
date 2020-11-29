#Write a program that takes a list and returns a new list that contains all the elements
# of the first list minus all the duplicates.

a = list()
a = [1,4,3,1,2,4,5,9]
n = len(a)

for i in range (n-1):
    for j in range(n-1):
        if a[i] == b[j]