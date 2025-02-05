    # Map applies a function to all the items in an input_list.
"""map(function, input_list)"""
# the function can be lambda function
# map doesnt store any data, it points to the memory location in RAM
# convert map object to desired data types to print actual data.
#map iterates over a set of data present in the list and similar data types.
#In Python, filter and map are higher-order functions used to process collections (like lists, tuples, etc.), 
# but they serve different purposes:
from functools import reduce

l_string=["1","2",'3','4']
print(l_string)
l_int = list(map(int,l_string))
print(l_int)


l1= [1,2,3,4,5]
square = lambda x: x*x
l1_square = list(map(square,l1))
print(l1_square)

#### Filter #####
"""
filter(function, iterable)
function: A function that returns a boolean value.
iterable: The collection to filter.
Only the elements for which the function returns True are included in the output.
Returns a filter object (an iterator).
"""

nums = [1, 2, 3, 4, 5]
result = filter(lambda x: x % 2 == 0, nums)
print(list(result))  # Output: [2, 4]


### Reduce ###
"""
Reduce applies a rolling computation to sequential pair of elements
The reduce function in Python is used to apply a function cumulatively to the items of an iterable (like a list), 
reducing the iterable to a single value. It is part of the functools module

The reduce function reduces an iterable to a single value.
It is useful for cumulative operations like summation, product, or concatenation.

Use it for operations where you need to combine all elements of an iterable into a single value.
However, for readability, explicit loops or built-in functions like sum() or prod() (from Python 3.8) are often preferred.

How it Works:
1.The reduce function applies the function to the first two elements of the iterable.
2.Then it takes the result and applies the function to it and the next element.
3.This process continues until all elements are processed, and a single result is returned.

from functools import reduce
reduce(function, iterable[, initializer])

"""

nums = [1, 2, 3, 4, 5]
result = reduce(lambda x,y: x+y, nums)
print(result)  # Output: 15