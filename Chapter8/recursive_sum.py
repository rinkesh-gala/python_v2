# Write a recursive function to calculate the sum of first n natural numbers


def recursive_sum (n):
    if (n==1):
        return 1
    else:
        return (n+recursive_sum(n-1))
    

n=int(input("enter a number: "))
print(f"sum of numbers is {recursive_sum(n)}")