#Write a program that stores birthdays information about friends. If there is no name on list
#program should add it
birthdays = {'Tom':'25 January','Mark':'15 December','Alice':'08 April'}
question1 = ""

name = str(input("Who's birthday are you looking for? (blank for break)"))
while name !="":
    if name in birthdays:
        print(name, " birthday is on ", birthdays[name])
    else:
        print("There is not info about ", name, "bithday. Would you like to add this name to list? (Y/N)")
        question1 = input()

    if question1 == "Y":
        print("When is", name, "birthday?")
        new_bd = input()
        birthdays[name] = new_bd
        question1 = ""

    name = str(input("Who's birthday are you looking for? (blank for break)"))
