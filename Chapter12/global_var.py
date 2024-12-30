#‘global’ keyword is used to modify the variable outside of the current scope


def fun():
    global a  # now this will star refering to global a variable which is outside of the function
    print(f"printing from inside the function: {a}")
    print(f"changing the value of \"Global a\" from the function...")
    a=10
    print(f"printing from inside the function after changing the value: {a}")
    
a=90
print(f"printing from outside of the function: {a}")
fun()
print(f"printing from outside the function after changing the value: {a}")

