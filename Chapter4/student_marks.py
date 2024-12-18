#accept marks of 6 students and display them in a sorted manner

marks_str_list = input("enter marks separated by space:").split()
marks_int_list = list(map(int,marks_str_list))
marks_int_list.sort(reverse=True)
print(type(marks_int_list))
print(marks_int_list)