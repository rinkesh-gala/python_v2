# . Write a program to filter a list of numbers which are divisible by 5

divisible_5 = lambda x: x%5==0

list_divisble5 = list(filter(divisible_5,range(1,101)))
print (list_divisble5)

