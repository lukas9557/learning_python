#User input a value and program returns values from list (a) that are less than user's number

a = [5, 8, 13, 21, 34, 55, 89, 1, 1, 2, 3]
n = len(a)
x = int(input("Give a value: "))
b=list()

for i in range (n):
    if a[i] < x:
        b.append(a[i])

print(b)
