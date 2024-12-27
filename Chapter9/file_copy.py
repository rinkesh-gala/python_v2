# Write a program to make a copy of a text file “this. txt”

import shutil

source = "file_copy.txt"
destination = "file_copy1.txt"
shutil.copyfile(source,destination)
print("File copied successfully")