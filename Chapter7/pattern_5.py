"""
print the pattern
1
10
101
1010
10101
"""

for i in range(1,6):
    for j in range(1,i+1):
        print(j%2,end="")
    print()

