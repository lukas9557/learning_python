#Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write
# a prgoram that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = list()
n = len(a)

for i in range(n-1):
    if a[i]%2 == 1:
        b.append(a[i])

print(b)