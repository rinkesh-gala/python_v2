# Write a program to find the sum of first n natural numbers using while loop.

num = int(input("enter a number:"))
i =1 
sum = 0

while(i<=num):
    sum += i
    i +=1

print(f"sum of all the natural number till {num} is : {sum}")

# there is a math formula to find sum of natural number n * (n + 1)/2

print(f"using formula : {((num*(num+1))/2)}")
