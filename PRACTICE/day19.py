# 1. Write a python program to identify unique triplets whose three elements sum to zero from 
# an array of n integers

def find_triplets(list1, n):  
    triplets = []  
    found= False  
    for i in range(0, n-2):  
        for j in range(i+1, n-1):  
            for k in range(j+1, n):  
                if (list1[i] + list1[j] + list1[k] == 0):  
                    triplets.append([list1[i], list1[j], list1[k]])  
                    found = True  
    if (found == False):  
        print(" not exist ")  
    return triplets  
list1 = [-10, 0, 10, 30, -10, -30, 60]  
n = len(list1)  
print(find_triplets(list1, n))


# 2. Write a python program to make combinations of 3 digits
num1=int(input("enter number"))
num2=int(input("enter number"))
num3=int(input("enter number"))
combination=[]
combination.append(num1)
combination.append(num2)
combination.append(num3)

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j & j!=k & k!=i):
                print(combination[i],combination[j],combination[k])

# 3. Pattern print 
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *
n = 5

# Upper part of the pattern
for i in range(n):
    spaces = " " * (n - i - 1)
    if i == 0:
        print(spaces + "*")
    else:
        stars = " " * (2 * i - 1)
        print(spaces + "*" + stars + "*")

# Lower part of the pattern
for i in range(n - 2, -1, -1):
    spaces = " " * (n - i - 1)
    if i == 0:
        print(spaces + "*")
    else:
        stars = " " * (2 * i - 1)
        print(spaces + "*" + stars + "*")


