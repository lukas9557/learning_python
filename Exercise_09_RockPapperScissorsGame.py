#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new game)
PA = "Y" #play again?
print("Let's play Rock-Paper-Scissors")
PO = ""
PT = ""

while PA == "Y":
    PO = str(input("Player 1 turn. What do you choose? "))  # Player one
    while PO not in ("rock", "paper","scissors"):
        PO = str(input("Wrong input! Player 1 turn. What do you choose? (rock/paper/scissors) ")) #Player one

    PT = str(input("Player 2 turn. What do you choose? "))  # Player one
    while PT not in ("rock", "paper", "scissors"):
        PT = str(input("Wrong input! Player 2 turn. What do you choose? (rock/paper/scissors) "))  # Player one

    if PO == "rock":
        if PT == "rock":
            print("It's a draw.")
        elif PT == "paper":
            print("Player 2 won.")
        else:
            print("Player 1 won.")
    elif PO == "paper":
        if PT == "rock":
            print("Player 1 won.")
        elif PT == "paper":
            print("It's a draw.")
        else:
            print("Player 2 won.")
    elif PO == "scissors":
        if PT == "rock":
            print("Player 2 won.")
        elif PT == "paper":
            print("Player 1 won.")
        else:
            print("It's a draw.")

    PA = str(input("Do you want to play again? (Y/N) "))
    if PA == "Y":
        print("Let's play again!")
    else:
        print("Thank you.")
        exit()
