

# * * * * *
#  * * * * *
#   * * * * *
#    * * * * *
#     * * * * *

num=int(input("row"))#number of row5
for i in range(num,0,-1):#row
    for j in range(-1,num-i-1):#space
        print(end=" ")
    for j in range(0,num):#coloumn
        print("*",end=" ")
    print()













num=int(input("row"))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()



num=int(input("row"))
for i in range(num,0,-1):
    for j in range(0,num-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()