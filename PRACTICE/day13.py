# 1. Write a Python program that Use while loop to display elements from a given list present
#  at odd index positions
lst=[2,3,4,5,6,7,8,9,11,23,45,66,44,89]
index=1
while index < len(lst):
    print(lst[index])
    index+=2

# or
lst=[]
for i in range(6):
 user_input=int(input("enter the number"))
 lst.append(user_input)
print(lst)
index=1
while index < len(lst):
    print(lst[index])
    index+=2

# 2.Write a python program that Take input from user and make square list of the number 
# and the cube list .Range is 10 number in the list
lst=[]
sq_lst=[]
cube_lst=[]
for i in range(5):
   user_input=int(input("enter number")) 
   lst.append(user_input)
for num in lst:
   sq=num**2
   cube=num**3
   sq_lst.append(sq)
   cube_lst.append(cube)

print(lst)
print(sq_lst)
print(cube_lst)


# 3.Pattern print 
# 1 
# 1 2 1 
# 1 2 3 2 1 
# 1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1
rows = 6
for i in range(1, rows + 1):
    for j in range(1, i - 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()