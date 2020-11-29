#Exercise from book Automate the boring stuff with Python
#Program should convert spam list to string, and separate each value with comma instead of last two.
#Last two valuest should be separated with "and". Eg. spam = ['apples', 'bananas', 'tofu', 'cats] should
#convert to string spam = apples, bananas, tofu and cats
spam = ['apples', 'bananas', 'tofu', 'cats', 'hello', 'beer']
new_spam = list()
n = len(spam)

for i in range(0,n-1):
    if i <= n-3:
        new_spam.append(spam[i])
        new_spam.append(", ")
    elif i == n - 2:
        new_spam.append(spam[i])
        new_spam.append(" and ")
        new_spam.append(spam[i+1])

x = ""
for i in new_spam:
    x += i

print(x)
