#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell
# them whether they guessed too low, too high, or exactly right.

UN = int() #User number
GN = int() #Random Number
i = int()
i = 1

import random
GN = random.randint(0,9)
#print(GN)

while UN != GN:
    UN = int(input("Guess the number beetwen 1 and 9: "))
    if UN > GN:
        print("Too much")
        i = i + 1
    elif UN < GN:
        print("Not enough")
        i = i + 1

if i == 1:
    T = "time"
else:
    T= "times"

print("Congratulations! My number is: ", GN, "\nYou guessed number in ", i, T)

PA = str(input("Do you want to play again? (Y/N) "))
if PA == "Y":
    print("Let's play again!")
else:
    print("Thank you.")
    exit()
