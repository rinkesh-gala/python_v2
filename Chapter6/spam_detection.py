# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

message = (input("enter a message:")).lower()
if ((message.find("make a lot of money") != -1) or (message.find("buy now") != -1) or (message.find("subscribe this") != -1) or (message.find("click this") != -1)):
    print("spam comment") # if (message in "make a lot of money") in operator can also be used to find substring in a string
else:
    print("not a spam comment") 
