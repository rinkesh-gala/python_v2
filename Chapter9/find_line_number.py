# Write a program to find out the line number where python is present in the file


with open("find_line_number.txt") as file:
    line_list = file.readlines()
    line_number=0

    for line in line_list:
        line = line.lower()
        line_number += 1
        if ("python" in line ):
            print(f"python word found at line {line_number}")
            
    if (line_number==0):
        print("python word not present in the file")