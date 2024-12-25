"""
print the pattern
5
44
333
2222
11111
"""


def pattern(n):
    for i in range(n,0,-1):
        for j in range(i,n+1):
            print(i,end="")
        print("")

n=int(input("enter a number: "))
pattern(n)           