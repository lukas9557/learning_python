#Strong password generator
lowercaseLetters = list()
uppercaseLetters = list()
numbers = list()
special = list()
all = list()
output = str()

import string
lowercaseLetters = list(string.ascii_lowercase)
uppercaseLetters = list(string.ascii_uppercase)
numbers = ["0","1","2","3","4","5","6","7","8","9"]
special = list(string.punctuation)
all = lowercaseLetters + uppercaseLetters + numbers + special
n = len(all)

x = int(input("How many characters should have your password? "))
import random
for i in range(x):
    y = random.randint(0,n)
    output = output + all[y]

print("Your password is: ", output)