#Write a program to store seven fruits in a list entered by the user

fruit_list = [fruit.strip() for fruit in input("enter list of fruits comma separated:").split(",")]
print(fruit_list)
print(type(fruit_list))