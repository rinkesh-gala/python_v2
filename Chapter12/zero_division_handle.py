# . Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionError’.

a= int(input("enter a numerator: "))
b= int(input("enter a denominator: "))

try:
    c= a/b
except ZeroDivisionError as e:
    print("number can't be divided by zero, answer is undefined")
else:
    print(f"{a}/{b}={c:.2f}")