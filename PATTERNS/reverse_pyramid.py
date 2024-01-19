#    * * * * *
#     * * * *
#      * * *
#       * *
#        *


num=int(input("row"))
for i in range(num):
    for j in range(num-i-1):
        print("",end=" ")
    for j in range(i+1):
     print("*",end=" ")
    print()
for i in range(num,0,-1):#row
    for j in range(0,num-i):#space
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
    # num=int(input("row"))





