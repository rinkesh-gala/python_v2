"""
print the pattern
5
45
345
2345
12345
"""


for i in range(5,0,-1):
    for j in range(i,5+1):
        print(j,end="")
    print()
