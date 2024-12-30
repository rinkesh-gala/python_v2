# Write a python program using function to convert Celsius to Fahrenheit

def c_f(c: float) -> float:
    return ((c*9/5)+32)

c= float(input("enter a number: "))
print(f"Fahrenheit equivalent of °{c}C is °{c_f(c)}F")