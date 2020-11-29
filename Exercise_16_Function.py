#Easy exercise to practise functions in Python. Function returns difference between two values
#given by user

def liczby(x,y):
    if x == y:
        return("Values are equal.")
    else:
        z = ("Difference between your values is: ", str(abs(x-y)))
        return(z)

x = int(input("Tell me please, what is your first number: "))
y = int(input("And seconf one? "))
print(liczby(x,y))
