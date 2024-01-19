# o                     1               1 OR Odd= O
# o E                   1 2             2%2!=0==E even=E
# o E o                 1 2 3
# o E o E               1 2 3 4
# o E o E 0             1 2 3 4 5

for row in range(1,6):
    for col in range(1,row+1):
        print("o"if col %2!=0 else "E",end="  ")
    print()