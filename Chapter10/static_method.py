# Add a static method to greet the user with hello.

class Demo:
    
    @staticmethod # this is called as decorator. there are other decorator as well
    def greet(): #static methods are used when you dont want to operato on object attribute rather on classes level attributes
        print("welcome to the world of Python Classes") #or anything which is not related to object attributes

d1 = Demo()
d1.greet()

