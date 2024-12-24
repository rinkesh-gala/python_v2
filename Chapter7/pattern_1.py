# Write a program to print the following star pattern.
"""
  *
 ***
***** 

"""


rows =int (input("enter a numer: "))

for i in range(1,rows+1):
  print(" "*(rows-i),end="") # end="" will make sure after print command cursor doesnt go to next line
  print("*"*(2*i-1))      # number of stars are increasing by two in every line in odd numbers. hence we can used odd number sequence 2n-1
