#Program tells if the name given by user is male or female (in Polish each female name ends with "a").

def plec(imie):
    n = len(imie)
    if(imie[n-1] == "a"):
        return("Woman")
    else:
        return("Men")

print(plec(imie = str(input("Jak masz na imię? "))))
