#Check that a tuple type cannot be changed in python

tuple_1 = (1,2,3,"rinkesh",None, True) # tuples are immutable, you cant make modification in it just like string data type
list_1 = list(tuple_1)
print(type(tuple_1))
print(type(list_1))