# Write a list comprehension to print a list which contains the multiplication table of a
# user entered number. store the table in a file named Tables.txt

n =5 
with open("table.txt","w") as file:
    table = [i*n for i in range(1,11)]
    print (table)
    file.write(str(table))
