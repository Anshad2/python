    
 #list# algorithams

# [] is square bracket
# insertion order preserved
# duplication allowed
# index positopn from 0 to...call by[..]
# update possible
#         0       1      2       3      4     5      6         7(index position)
colours=["red","green","blue","white","red","blue","violot","yellow"]
print(colours)
print(colours[2])#index position 2 is blue

colours[1]="purple"# at the positon 1 is green is replaced by "purpple"
print(colours)#updates possible
        #  0     1    2    3   4     5    6    7
expenses=[1200,2300,3400,5600,8000,4500,1200,3000]
print(expenses[3])
expenses[0]=2000
print(expenses)

print(len(expenses))

# 
for i in range(0,len(expenses)):
    print(expenses[i])
# 
for exp in expenses:
    print(exp)

# print all expenses above 4000
for i in range(0,len(expenses)):
    if expenses[i]>4000:
        print(expenses[i])

# print all expenses in range of 1

