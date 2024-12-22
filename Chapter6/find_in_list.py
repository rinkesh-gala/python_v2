# Write a program which finds out whether a given name is present in a list or not.

name_list =["rinkesh","manish","vishal","nikita","mehul"]
user_name = input("enter a name to search in list:")
if (user_name in name_list):
    print("user present in the list")
else:
    print("user not present in the list")