# *
# * * *
# * * * * *

num=int(input("num of row"))
k=1
for i in range(1,num+1):
    for j in range(1,k+1):
        print("*",end=" ")
    k=k+2
    print()



def pattern_print(n):
    # First triangle
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(i+1):
            print("*", end="")
        print()

    # Second triangle
    for i in range(n-1, -1, -1):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(i+1):
            print("*", end="")
        print()

n = 7
pattern_print(n)

