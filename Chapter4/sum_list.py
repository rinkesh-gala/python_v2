#Write a program to sum a list with 4 numbers

marks_str_list = input("enter marks separated by space:").split()
marks_int_list = list(map(int,marks_str_list))

print(sum(marks_int_list))