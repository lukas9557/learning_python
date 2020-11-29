#Program indicates numbers that you can divide your number by, and receive intiger values

n = int(input("Give a number: "))

for i in range (1,n+1):
    if n%i == 0:
        print(i)
