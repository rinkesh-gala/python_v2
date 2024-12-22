#Write a program to find the greatest of four numbers entered by the user.

a = int (input("enter first number:"))
b = int (input("enter second number:"))
c = int (input("enter third number:"))
d = int (input("enter fourth number:"))

if(a>b and a>c and a>d):
    print(f"{a} is greatest amongs all")
elif(b>c and b>d):
    print(f"{b} is greatest among all")
elif(c>d):
    print(f"{c} is greatest among all")
else:
    print(f"{d} is greatest among all")


