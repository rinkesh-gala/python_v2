"""
Write a python function to print first n lines of the following pattern:
***
** 
*
"""
# #approach1
# def print_pattern(n):
#     for i in range(n,0,-1):
#         print("*"*i)

#n = int(input("enter a number: "))
# print_pattern(n)

#approach2 using recursion
def print_recursion(n):
    if (n==0):
        return 
    print("*"*n)
    print_recursion(n-1)

n = int(input("enter a number: "))
print_recursion(n)