#Ask the user for a number and determine whether the number is prime or not.

UN = int(input("Give a number: "))
a = list()

for i in range(1,UN+1):
    if UN % i == 0:
        a.append(i)

b = str()

if len(a) == 2:
    print("Your number is prime. You can divide it by 1 and", UN)
else:
    for i in range(len(a)):
        b = b + str(a[i]) + ","
    print("Your number is not prime. You can divide it by:", b)