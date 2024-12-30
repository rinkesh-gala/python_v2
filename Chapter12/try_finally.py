# # TRY WITH FINALLY
# Python offers a ‘finally’ clause which ensures execution of a piece of code inspective of
# the exception. you might ask code still gets executed when its written after try-exception block.
# but in case of function when it has return block this doesnt happen.
#finally overwrites everything and gets executed

def main():
    try:
        a = int(input("enter a number: "))
        print(a)
        return 
    except Exception as e:
        print(e)
        return
    finally:
        print("you are in Finally block")

main()

"""
output1
enter a number: 1
1
 you are in Finally block

 
output2
enter a number: asda
invalid literal for int() with base 10: 'asda'
you are in Finally block

"""