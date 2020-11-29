#Cows and Bulls game. Here are rules of the game: https://en.wikipedia.org/wiki/Bulls_and_Cows

#Generating a 3digit number
import random
num = random.randint(100,999)
print("Computer's number:",num) #to be commented
num2 = [int(x) for x in str(num)]
print("Computer's number as a list:", num2)

#Guessing number by user
UN = 0
cows = 0
bulls = 0
while num != UN:
    UN = int(input("Guess the number between 100 and 999: "))
    UN2 = [int(x) for x in str(UN)]
    print(UN2)
    if UN < 100 or UN > 999:
        print("Your number is not between 100 and 999. Type number again.")
    else:
        for i in range(3):
            for j in range(3):
                if num2[i] == UN2[j]:
                    if i == j:
                        cows +=1
                    elif i != j:
                        bulls +=1
    print("Cows: ", cows)
    print("Bulls: ", bulls)

print("Congratulations, you've guessed the number.")