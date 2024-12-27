# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class Modification:
    a = None

a1 = Modification()
a1.a = 0 # sets attribute at object level

a2 = Modification()

print(a1.a) 
print(a2.a) # default value taken from the class attribute
print(Modification.a) # class attirbute still doesn't changes as we were operating on instance level and not at class level

Modification.a = 100 # this has class attribute to 100 now
print(Modification.a)

a3 = Modification() # in last line class attribute was set, now all new object will take newly set class attribute value 
print(a3.a) # hence output of this will be 100 and not 4