#        1
#      2 1
#    3 2 1
#  4 3 2 1
#5 4 3 2 1

n=int(input("number of row"))
for i in range(n):#row
    for j in range(n-i-1):#space
        print(" ",end=" ")
    for j in range(i+1):#coloumn
        print(j+1,end=" ")
    print()