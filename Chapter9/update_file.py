# A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file

import fileinput
keyword_find = "donkey"
keyword_replace = "######"

#approach1
# with open("update_file.txt") as file_open:
#     file_read =(file_open.read()).lower()

# file_modified =file_read.replace(keyword_find, keyword_replace)

# with open("update_file.txt","w") as file_open:
#     file_open.write(file_modified)

# print("File has been modified")

#approach2
#Python's fileinput module allows you to modify files in place while iterating through them.

for line in fileinput.input("update_file.txt",inplace=True): 
    line_lower = line.lower()
    if (keyword_find in line_lower):
        line_lower = line_lower.replace(keyword_find,keyword_replace)
    print(line_lower,end="")    