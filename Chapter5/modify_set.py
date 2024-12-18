# Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

s = {8, 7, 12, "Harry", [1,2]}



# You cannot use a list as an element of a set in Python because lists are mutable and therefore not hashable. 
# Sets in Python require their elements to be immutable (hashable) to ensure uniqueness and allow operations like membership testing efficiently

# Use a tuple instead of a list if you need something similar but immutable:
# s = {8, 7, 12, "Harry", (1, 2)}

