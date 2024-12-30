a= int(input("enter a number: "))
b= int(input("enter a number: "))

if ( b!=0):
    print (a/b)
else:
    raise ZeroDivisionError("number can't be divided by zero") # this will terminate further execution of
                           # program. this is sometime needed to make developer aware that they are doing something wrong
                           # this used in library development so that consumers of librarires alerted when something is 
                           # not aligned      
print("program ends")