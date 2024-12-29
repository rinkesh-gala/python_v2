# Write a class vector representing a vector of n dimensions. Overload the + and *
# operator which calculates the sum and the dot(.) product of them.


import math

class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def __add__(self,sec_num):
        return Vector(self.x+sec_num.x,self.y+sec_num.y,self.z+sec_num.z)
    
    def __mul__(self,sec_num):
        return (self.x*sec_num.x+self.y*sec_num.y+self.z*sec_num.z)
    
    def __str__(self):
        if (self.y>0 and self.z >0):
            return (f"{self.x}i+{self.y}j+{self.z}k")
        elif (self.y<0 and self.z>0):
            return (f"{self.x}i{self.y}j+{self.z}k")
        elif(self.y>0 and self.z<0):
            return (f"{self.x}i+{self.y}j{self.z}k")
        else:
            return (f"{self.x}i{self.y}j{self.z}k")

v1=Vector(-1,-2,-3)
v2=Vector(4,5,6)
print(v1+v2)
print(v1*v2)
