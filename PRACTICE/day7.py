# 1. Write a Python program that separate positive and negative numbers from a list
# main_list=[-1,2,3,4,5,-9,-4,-8]
# pos_list=[num for num in main_list if num >=0]
# neg_list=[num for num in main_list if num <0]

# print(f"positive list is {pos_list}")
# print(f"negative list is {neg_list}")

# # or
# my_list=[]
# positive=[]
# negative=[]
# n=int(input("enter your length of list"))
# for i in range(0,n):
#     value=int(input("enter your number"))
#     my_list.append(value)
# for i in range(n):
#     if my_list[i] >= 0:
#      positive.append(my_list[i])
#     else:
#        negative.append(my_list[i])
# print(f"All numbers is {my_list}")
# print(f"All positive numbers is {positive}")
# print(f"All negative numbers is {negative}")


# # 2.Write a python program to reverse the tuple
# reversed is a built function in tuple
# x=("w3school")
# y=reversed(x)
# print(tuple(y))


# or
tpl=(10,20,30,40,50,60,70,80,90)
rvs_lst=[]
rvs_tpl=()
for n in tpl:
    rvs_lst.insert(0,n)
rvs_tpl=tuple(rvs_lst)
print(rvs_tpl)

# 3.Pattern print
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3 
# 4 4  
# 5

# /rows=int(input("number of row"))# for number of rows
# # n=5
# for i in range(1,rows+1):#row
#     for j in range(rows-i+1):#coloumn
#         print(i,end=" ")
#     print()