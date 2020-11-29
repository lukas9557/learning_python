#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome
# is a string that reads the same forwards and backwards.)
a = str(input("Give a string: "))
n = len(a)
b = list()
i = 0
int(i)

for i in range(n-1,-1,-1):
    b.append(a[i])

#print(str(b))
c = ""
for i in range(n):
    c = c + b[i]

print("Your string in reverse is: ", str(c))

if a == c:
    print("It's a palindrome!")
else:
    print("It is not a palindrome")
