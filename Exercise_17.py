#User give a string to program, then user indicate position which to replace, and with what.
def change(text,pos):
    n = len(text)
    if pos > n:
        print("String is shorter than position you wanna replace.")
        exit()
    elif pos == n:
        new = input("Give a new character: ")
        return(text[:n-1] + new)
    else:
        new = input("Give a new character: ")
        return(text[:pos-1] + new + text[pos:])

text = input("Give a string: ")
pos = int(input("Wchich position do you want to replace? "))
print(change(text, pos))