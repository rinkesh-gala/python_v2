# There are many built-in exceptions which are raised in python when something goes
# wrong.
# Exception in python can be handled using a try statement. The code that handles the
# exception is written in the except clause.

#
try:
    a=int(input("enter a number:"))
    print(a)
except Exception as e: # exception helps to prvent further programing termination because of some exception. 
    print(e)   # even if users enter non integer as input program will catch that exception, display the message and 
                 # continue with execution of rest of code.   
                 # this will error as "ValueError: invalid literal for int() with base 10"    
print ("thanks")

#mention specific error rather than system generated error in the exception block
# catch specific errors, you can also have multiple except block written
try:
    b=int(input("enter a number: "))
except ValueError:
    print("you have entered invalid input")

print ()