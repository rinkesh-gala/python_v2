#print content of directory using OS module 
import os

dir_path ="/"

#approach-1
print(os.listdir(dir_path))

#approach-2
content = os.listdir(dir_path)
for items in content:
    print (items)

