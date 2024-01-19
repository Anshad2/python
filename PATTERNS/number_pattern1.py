# Q?
# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1
n=int(input("number of row"))
for i in range(n):#row
    for j in range(i+1):
        print(n-i,end=" ")
    print()

# Q?
# 5
# 5 4
# 5 4 3
# 5 4 3 2 
# 5 4 3 2 1

n=int(input("number of row"))
for i in range(n):
    for j in range(i+1):
        print(n-j,end=" ")
    print()


