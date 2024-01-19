# 1. Write a python program to find the sum of elements in a tuple
tpl=(1,3,5,7,3,9,7,5,8)
sum=0
for num in tpl:
    sum=sum+num
print(sum)

# or
# tpl=(1,2,3,4,5,7)
# tpl_sum=sum(tpl)
# print(tpl_sum)


# or
# tpl=()
# my_lst=list(tpl)
# sum=0
# limit=int(input("enter the limit of tuple"))
# for i in range(limit+1):
#     user_input=int(input("enter number"))
#     my_lst.append(user_input)
#     sum=sum+user_input
# print(sum)

# 2.Convert tuple to a list and find sum
tpl=(1,2,3,4,5,6,7)
sum=0
my_lst=list(tpl)
for num in tpl:
    sum=sum+num
print(sum)


# or
# tpl=()
# my_lst=list(tpl)
# sum=0
# limit=int(input("enter the limit of tuple"))
# for i in range(limit+1):
#     user_input=int(input("enter number"))
#     my_lst.append(user_input)
#     sum=sum+user_input
# print(sum)

# 3. Pattern print 
# A 
# B B 
# C C C 
# D D D D 
# E E E E E

num=5#how many rows want
A=65
for i in range(num):#row
   for  j in range(i+1):#coloumn
    print(chr(A),end=" ")
   A+=1
   print()
