# The ‘enumerate’ function adds counter to an iterable and returns it
#The enumerate object yields pairs containing a count (from start, which defaults to zero) and 
# a value yielded by the iterable argument.
# enumerate is useful for obtaining an indexed list:
#     (0, seq[0]), (1, seq[1]), (2, seq[2]), ...

l= [45,243,575,2423,23423]

#without enumerate. you have to explicitly manage another variable for the index
index =0
for item in l:
    print(f"index is {index}, item is {item}")
    index +=1


# with enumerate function. 
print("\nnow using enumeration...\n")
for index, item in enumerate(l):
    print(f"index is {index}, item is {item}")
