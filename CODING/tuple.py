# fruits = ['apple', 'banana', 'cherry']  
# print("fuirts[1] =", fruits[1])  
  

Set_List = [  
    {1, 2, 3, 1},  
    {4, 7, 2, 9},  
    {5, 7, 6},  
    {3, 1, 2},  
    {6, 7, 5, 4},  
    {6, 7, 5, 5}  
]


# duplicates = []

# for i in range(len(Set_List)):
#     for j in range(i + 1, len(Set_List)):
#         if Set_List[i] == Set_List[j]:
#             duplicates.append(Set_List[i])

# print("Duplicates:", duplicates)

list1 = [12, 14, 16, 18, 20]  

# repitaion

print(list1*2)


list1 = [1,5,2,9,10,3,4,10,5,9,6]

list1.sort(reverse=True)

set_lst = set(list1)

u=list(set_lst)

u.reverse()

print(u[1])




Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday", "Sunday"}    
print(Days1-Days2)


# sum of list
lst = [1,3,4,5,6,7,8]

sum_lst = sum(lst)

print(sum_lst)



# How to compare two lists in Python

list1 = [11, 12, 13, 14, 15]  
list2 = [11, 12, 13, 14, 15] 

if list1==list2:

    print(True)

else:

    print(False)

