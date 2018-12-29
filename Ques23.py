#Ques.23

X = input("Enter your string:\n")
l=len(X)
print("The length is",l)
Y = "Anjali"
Z =X+Y
print("After concatenation", Z)
print(''.join(reversed(X)))
old="I like Python"
new=old.replace("like","love")
print (new)
if X== Y:
    print("Equal")
else:
    print("Not Equal")