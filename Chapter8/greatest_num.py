# Write a program using functions to find greatest of three numbers.

def great_num(a: int,b: int,c: int) -> int :
    if (a>b and a>c):
        return a
    elif (b>c):
        return b
    else:
        return c

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
print(f"greatest of 3 number is: {great_num(a,b,c)}")