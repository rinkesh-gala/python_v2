# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class TwoD:
    x = None
    y= None

    def __init__(self,x,y): ## any function which preceeds with two underscore is called as dunder function
        self.x = x
        self.y = y
    
class ThreeD(TwoD):
    z=None

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z =z


a_2d = TwoD(10,10)
b_3d = ThreeD(20,20,20)

print (b_3d.x, b_3d.y, b_3d.z)
print (a_2d.x, a_2d.y)
