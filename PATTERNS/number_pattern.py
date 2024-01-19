# 15
# 14 13
# 12 11 10
# 9  8  7  6 
# 5  4  3  2  1

# right traingle 
n=int(input("row"))
k=0
for i in range(n):
    k=k+i
m=n+k
for i in range(n):
    for j in range(i+1):
        print(m,end=" ")
        m=m-1
    print()


