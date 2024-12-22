# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F



marks = int(input("enter your marks to derive grade:"))
if (marks >100):
    print("enter valid marks")
elif (marks >=90):
    grade = "Ex"
    print(f"your grade is {grade}") 
elif (marks>=80):
    grade = "A"
    print(f"your grade is {grade}") 
elif(marks>=70):
    grade = "B"
    print(f"your grade is {grade}") 
elif(marks>=60):
    grade="C"
    print(f"your grade is {grade}") 
elif(marks>=50):
    grade="D"
    print(f"your grade is {grade}") 
else:
    grade="F"
    print(f"your grade is {grade}") 

   