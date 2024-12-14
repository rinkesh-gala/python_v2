# Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
from datetime import date

name = input("enter your name:")
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>",name).replace("<|Date|>",str(date.today()))) 
#use replace functionn twice. modify output of first replace function with the use of second replace function. this is called as chaining of functions
#date.today will return value in datetime.date type which can not be used along with string operations hence we need to convert date in String
