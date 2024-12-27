# Write a class “Calculator” capable of finding square, cube and square root of a number
import math

class Calculator:
    def __init__(self,num):
        self.num = num

    def square(self):
        return self.num * self.num
    
    def cube(self):
        return math.pow(self.num,3)
    
    def square_root(self):
        return math.sqrt(self.num) # can be written as self.num**1/2 (** means power to )

num1 = Calculator(10)
print(f"square of {num1.num} is {num1.square()}")
print(f"cube of {num1.num} is {num1.cube()}")
print(f"square root of {num1.num} is {num1.square_root()}")