#important Concept

def extend_list(val,lst=[]):
    lst.append(val)
    return lst

list1 = extend_list(10)
list2 = extend_list(123,[])
list3 = extend_list("a")

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = {list3}")

"""
output of above program is

list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']
"""

"""
In Python, default argument values in functions are evaluated only once at the time the function is defined, 
not each time the function is called. If the default argument is mutable (like a list, dictionary, or set), 
any modification to it will persist across subsequent function calls, which can lead to unexpected behavior.

Mutable objects include lists, dictionaries, sets, and other objects that can be modified after their creation.
If a mutable object is used as a default argument, 
all function calls that don't provide that argument will share the same instance of the object.


Fixing the Issue
To avoid this behavior, use None as the default value and initialize the mutable object inside the function:
This ensures that each call gets its own independent list.

def extend_list(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    return lst

list1 = extend_list(10)
list2 = extend_list(123, [])
list3 = extend_list('a')

print("list1 = ", list1)  # Outputs: list1 =  [10]
print("list2 = ", list2)  # Outputs: list2 =  [123]
print("list3 = ", list3)  # Outputs: list3 =  ['a']


*Key Takeaways*
Avoid using mutable objects (e.g., lists, dictionaries) as default arguments in functions.
Use None as the default argument and initialize the mutable object inside the function.
This prevents unintended side effects and ensures each function call has its own independent instance of the object.

"""