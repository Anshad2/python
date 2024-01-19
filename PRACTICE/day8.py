# 1. Write a Python program to find n natural number in ascending order
# my_lst=[1,4,6,5,9,2,0,3,7,8]
# # my_lst1=["Python", "Swift","Java", "C++", "Go", "Rust"]
# my_lst.sort()
# # my_lst1.sort()
# print(my_lst)
# # print(my_lst1)

# # or
# # for numbers only
# num=int(input("no of terms needed"))
# lst=[]
# for i in range(num):
#     value=input("enter values")
#     lst.append(value)

# lst.sort()
# print(lst)
starting=int(input("enter starting"))
ending=int(input("enter limit"))
if starting<ending:
    for i in range(starting,ending+1):
        print(i)
else:
    for i in range(ending,starting+1):
        print(i)


# 2.Write a python program to find n natural number in descending order
# ex_lst=[1,4,6,5,9,2,0,3,7,8]
# ex_lst.sort(reverse=True)
# print(ex_lst)

# # or
starting=int(input("enter starting"))
ending=int(input("enter limit"))
if starting>ending:
   for i in range(starting,ending-1,-1):        
      print(i)
else:
  for i in range(ending,starting-1,-1):
      print(i)
# # for numbers only
# num=int(input("no of terms needed"))

# lst=[]
# for i in range(num):
#     value=input("enter values")
#     lst.append(value)

# lst.sort(reverse=True)
# print(lst)

starting=int(input("enter starting"))
ending=int(input("enter limit"))
if starting>ending:
  for i in range(starting,ending-1,-1):        
   print(i)
else:
  for i in range(ending,starting-1,-1):
       print(i)


# 3.Pattern print 
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *

n=int(input("number of row"))
for i in range(n):#row
    for j in range(n-i-1):#space count
        print(" ",end=" ")#space
    for j in range(i+1):#coloumn
        print("*",end=" ")# what to print
    print()