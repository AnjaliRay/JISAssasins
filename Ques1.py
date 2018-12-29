#Ques7
n=int(input("Enter any number:"))
tot=0
while(n>0):
    dig=n%10
    tot+=dig
    n=n//10
print(tot)