# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "microsoft" #class attribute, common across all the object 
    def __init__(self,name,age,lang):
        self.name =name # object attributes
        self.age=age
        self.lang=lang
        print("Parameterised constructor executed successfully")

p1 = Programmer("rinkesh","33","python")
p2 = Programmer("vishal","34","salesforce")
print(p1.name, p1.age, p1.lang, Programmer.company) #class attirbute "company" can be accessed in two different ways
print(p2.name, p2.age, p2.lang, p2.company) #class attirbute "company" can be accessed in two different ways

