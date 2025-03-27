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

a=[1,4,3,5,8] 
b=[2,4,5,9,8]  
sorted_list = merge_sort(a+b)
print(f"{sorted_list=}")
print(f"duplicate removed {list(set(sorted_list))}")
