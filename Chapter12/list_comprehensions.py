# List Comprehension is an elegant way to create lists based on existing lists.
#do certain operation on existing list and store the result in another result in easy way.

list1 = [1,7,12,11,22]


# if you want to store square of each element from list1 in to list2 then you will apply for loop followed by list2.append
#this can be made easy using comprehension

list2 = [i*i for i in list1] # the variable i before and after for keyword has to be same. as it will take the value from for loop
print(list2)                 # once you have value in variable i, you can do operation on variable i and store the result in new list


list3 = [item for item in list1 if item >8]
print(list3)