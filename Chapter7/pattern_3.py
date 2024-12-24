"""
Write a program to print the following star pattern.
* * * 
*   * 
* * * 
print all the stars in first and last row. middle rows skip the stars
"""

rows =int (input("enter a numer: "))

for i in range(1,rows+1):
    if(i==1 or i==rows):
        print("*"*rows)
    else:
        print("*",end="")
        print(" "*(rows-2),end="")
        print("*")
