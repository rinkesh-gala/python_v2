# Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.


from pathlib import Path

def table(n,folder_path):
    file_name = str(folder_path)+"/"+str(n)+".txt"
    with open(file_name,"w") as content:
        for j in range(1,11):
            value = n * j
            value_string = str(n)+" x "+str(j)+" = "+str(value)+"\n"
            content.write(value_string)
    
folder_path = Path("table") # table is folder name, change it as per your need
folder_path.mkdir(parents=True,exist_ok=True)
current_directory = Path().cwd()

for i in range(2,21):
    table(i,folder_path)
print(f"all the tables from 2 to 20 have been saved under {current_directory}/{folder_path}/")