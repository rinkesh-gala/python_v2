# Write a program to print third, fifth and seventh element from a list using enumerate
# function.

l1= [34,54,"rinkesh",True,False,5839,-929.45,"bravo"]
index_list =[2,4,6]
for index,item in enumerate(l1):
    if(index in index_list):
        print(f"{item} is at index {index}")