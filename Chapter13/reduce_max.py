# Write a program to find the maximum of the numbers in a list using the reduce
# function.

from functools import reduce

def find_greater(a,b):
    if (a>b):
        return a
    else:
        return b
    
list1 = [10,20,45,12,9,9302,1209]
print(reduce(find_greater,list1))
