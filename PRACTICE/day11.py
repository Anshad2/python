# 1. Write a Python program that print 2 list and common element
# lst1=[9,4,3,10,15,12,13,1,2,4,5,7]
# lst2=[5,4,2,3,20,11,13,2,6,5,8,7]
# # without in
# lst1.sort()
# lst2.sort()
# p1,p2=0,0 # positon of elemnt
# while(p1<len(lst1) and p2<len(lst2)):

#   if lst1[p1]==lst2[p2]:
#    print(lst1[p1])
#    p1+=1
#    p2+=1
#   elif lst1[p1]< lst2[p2]:
#    p1+=1
#   else:
#    p2+=1

#    or

# lst1=[9,4,3,10,15,12,13,1,2,4,5,7]
# lst2=[5,4,2,3,20,11,13,2,6,5,8,7]
# print(set(lst1)&set(lst2))

# or

# lst1=["ant","man","cow","rat","mat","fat"]
# lst2=["hat","man","apple","vehicle","jump","fat"]
# print(set(lst1)& set(lst2))
# lst1.sort()
# lst2.sort()
# p1,p2=0,0
# while(p1<len(lst1) and p2<len(lst2)):
#     if lst1[p1]==lst2[p2]:
#      print(lst1[p1])
#      p1+=1
#      p2+=1
#     elif lst1[p1]< lst2[p2]:
#      p1+=1
#     else:
#      p2+=1
# or
# list1=[12,11,55,77,88,66,33,44,6]
# list2=[1,2,5,44,66,88,22,4,6]

# for i in  (list1):
#     for j in  (list2):
#         if i==j :
#             print(i, end=" ")
    


# 2.Write a python program to find the least square number from a list
# lst=[2,4,5,6,7,8,9]
# squares=[]
# for num in lst:
#     sq=num**2
#     squares.append(sq)
# print(squares)
# print(min(squares))

# 3.Pattern print 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

n=int(input("number of rows"))# number of row
for i in range(n):#for row
    for j in range(i+1):#coloumn
        print(j+1,end=" ")
    print()
