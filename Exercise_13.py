#Write a program that asks the user for a long string containing multiple
# words. Print back to the user the same string, except with the words in backwards order.
txt = str()
txt = input("Write something: ")
a = list()
a[:0]=txt
n = len(a)
b = list()
c = list()

print(n)
b.append(0)
for i in range(n):
    if a[i] == " ":
        b.append(i+1)
b.append(n)

print("b",b) #positions of space in string
m = len(b) #number of spaces
print("m", m)
print("n",n)

output = list()
for j in range(2,m+1):
    for i in range(b[m-j],b[m-j+1]):
        output.append(a[i])

print(''.join(output))