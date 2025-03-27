'''
a= [1,4,3,5,8] 
b=[2,4,5,9,8] 
Merge and sort without using any function. O/P should be [1,2,3,4,5,8,9]
'''

def merge_sort(c):
    for static_index in range(len(c)):
        for moving_index in range(static_index+1,len(c)):
            if (c[static_index]>c[moving_index]):
                c[static_index],c[moving_index]=c[moving_index],c[static_index]
    return c     

def remove_dup(sorted_list):
    dedup_list =[]
    for item in sorted_list:
        if item not in dedup_list:
            dedup_list.append(item)
    return dedup_list

a=[1,4,3,5,8] 
b=[2,4,5,9,8,-1]  
sorted_list = merge_sort(a+b)
#print(f"duplicate removed {list(set(sorted_list))}") # this doesn't work with negative numbers. 
# it gave output as [1, 2, 3, 4, 5, 8, 9, -1]
print(f"{sorted_list=}")
print(f"dedup list: {remove_dup(sorted_list)}")

