# # Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
# which changes the value of increment based on the salary.

class Employee:
    def __init__(self,name,salary): # any function which preceeds with two underscore is called as dunder function
        self.name = name             # here in this case this also called as constructor 
        self.salary = salary

    @property
    def salaryAfterIncrement(self):
         return self.salary * (1+self.increment/100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary) -1)*100
        print(self.increment)

e1= Employee("rinkesh",100)
e1.increment = 40
print(e1.salaryAfterIncrement)

e2 = Employee("vishal",100)
e2.salaryAfterIncrement = 200




