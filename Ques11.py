#Ques.11

x = input("Enter your string:")
y = input("Enter your character:")
count = 0

for i in x:
    if i == y:
        count = count + 1
print(count)
