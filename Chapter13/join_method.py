# Creates a string from iterable objects

l = ["apple", "mango", "banana"]
result = ", and, ".join(l)
print(result)
print(type(result))


#l1= [1,2,"rinkesh",None,True] # this gave below error
#r1= ",".join(l1) # TypeError: sequence item 0: expected str instance, int found
#print(r1) # list should have only str elements in it

