# Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
# present, a message without exiting the program must be printed prompting the same.

try:
    with open("file1.txt") as f1:
        pass
except FileNotFoundError as e: # can be written as "except Exception as e:" if you dont know exact error that will occure
    print(e, "file1 not present")

print("Program after try-except block to indicate program has not crashed")
print("thanks by developer")