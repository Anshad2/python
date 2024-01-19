# Q
# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5

n=int(input("row"))
for i in range(n):
    for j in range(i,-1,-1):
        print(n-j,end=" ")
    print()