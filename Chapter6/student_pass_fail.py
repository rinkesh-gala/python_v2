# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.


math = int(input("enter your math marks out of 100 :"))
sci = int(input("enter your science marks out of 100:"))
history = int(input("enter your history marks out of 100:"))
english = int(input("enter your english marks out of 100:"))

total_percentage = ((math+sci+history+english)/400)*100

if ( (math>=33 and sci >=33 and history>=33 and english >=33) and total_percentage >=40):
    print( f"student has passed. aggregate percentgae is {total_percentage}")
else:
    print("student has failed")    