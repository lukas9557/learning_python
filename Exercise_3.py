#User input a value and program returns values from list (a) that are less than user number

a = [5, 8, 13, 21, 34, 55, 89, 1, 1, 2, 3]
n = len(a)
x = int(input("Podaj liczbę: "))
b=list()

for i in range (n):
    if a[i] < x:
        b.append(a[i])

print(b)