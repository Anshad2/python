# Q?
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# nested for loop

n=int(input("number of rows"))# number of row
for i in range(n):#for row
    for j in range(i+1):#coloumn
        print(j+1,end=" ")
    print()

# Q?
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

n=int(input("number of row"))
for i in range(n):
    for j in range(i,-1,-1):
        print(j+1,end=" ")
    print()

# Q?
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


n=int(input("number of row"))
for i in range(n):# row
    for j in range(i+1):
        print(i+1,end=" ")
    print()

