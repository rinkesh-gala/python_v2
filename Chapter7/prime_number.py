# Write a program to find whether a given number is prime or not
# prime number is A natural number greater than 1 that has exactly two distinct positive divisors: 1 and itself

import sys
num = int(input("enter a number:"))
prime_check = 0

if (num<=1):
    print("not a prime number")
    sys.exit(0) # to exit from rest of the python program.

#approach 1
# for i in range(2,num):
#     if (num%i==0):
#         prime_check = 1

# if(prime_check == 0):
#     print("it is a prime number")
# else:
#     print("not a prime number")

#approach 2

for i in range(2,num):
    if(num%i==0):
        print("not a prime number")
        break
else:
    print("it is a prime number")    