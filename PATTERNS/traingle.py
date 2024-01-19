# input
# for loop()
# range(start,end)
# print()

# *
# * *
# * * *
# * * * *
# * * * * *

num=5#how many rows want
A=65
for i in range(num):#row
   for  j in range(i+1):#coloumn
    print(chr(A),end=" ")
   A+=1
   print()


   