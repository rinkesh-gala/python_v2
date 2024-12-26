file= open("file_op.txt","a")
content=file.write("\nhello")
content=file.write("\nhow are you\n")
file.close()

#other way to open the file is

with open("file_op.txt","a") as file_with: # you dont have to explicitly close the file when you use "With" statement
    file_with.write("written using with statment")
