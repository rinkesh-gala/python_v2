# Write a program to input eight numbers from the user and display all the unique numbers (once).

set_number = set(map(int,input("enter numbers separated by space:").split()))
print(set_number)