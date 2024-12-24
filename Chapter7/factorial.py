#Write a program to calculate the factorial of a given number using for loop

import math

num = int(input("enter a number:"))

#approach 1
factorial = 1
for i in range(1,num+1):
    factorial *= i

print(f"factorial is: {factorial}")


#approach 2
print(f"factorial using math fucntion {math.factorial(num)}")