# # TRY WITH ELSE CLAUSE 
# Sometimes we want to run a piece of code when try was successful

try:
    b=int(input("enter a number: "))
except ValueError:
    print("you have entered invalid input")
else:
    print("else got executed because try was successful")


print("program ends")


