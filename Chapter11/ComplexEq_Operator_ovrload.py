# Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.


class Complex:
    def __init__(self,real,img):
        self.real= real
        self.img = img

    def show_complex(self): # alternative is def __str__() dunder function
        if (self.img<0): # checking if imaginary part is negative then printing complex numbers accordinly
            print(f"{self.real}i{self.img}j") #because we need to decide what sign to put before printing imaginary number
        else:                                 # as we are concatinating strings while printing it.
            print(f"{self.real}i+{self.img}j") 

    def __add__(self,sec_num):
        return Complex(self.real+sec_num.real , self.img+sec_num.img)
    
    def __sub__(self,sec_num):
        return Complex(self.real-sec_num.real , self.img-sec_num.img)
    
    def __str__(self): # this will overload print statement over object instances, complex numbers in our case
        if (self.img<0): 
            return(f"{self.real}i{self.img}j") 
        else:                                 
            return(f"{self.real}i+{self.img}j")

num1 = Complex(-5,5)
num2 = Complex(10,-10)  
num3 = Complex(50,60)
num4 = Complex(30,-20)

num5 = num1 + num2
num6 = num1 - num2

num5.show_complex()
num6.show_complex()
print(num3+num4)