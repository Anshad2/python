# 1. Write a python program to create a list of tuples having first element as the number
#  and second element as the cube of the number

numbers=[1,2,3,4,5,6,7]
lst_of_tpl=[(num,num**3) for num in numbers]
print(lst_of_tpl)

# or



# 2. find the length of the string using for loop
word="Welcome to ooty nice to meet you"
length=0
for ch in word:
    length+=1
print(f"length of the string word : {length}")


# 3. Write a program to handling missing keys
# keys so it is dictionary
employee={"id":1998,"name":"anshad","dept":"IT","salary":60000}
if "exp" in employee:
    print(employee.get("exp"))
else:
    print("key not found")

    # or

# 4.Pattern print 
#         A 
#        B C 
#       D E F 
#      G H I J 
#     K L M N O
num=5
alphabets=65
for i in range(num):
    for j in range(num-i-1):# space
        print("",end=" ")
    for j in range(i+1):#col
     print(chr(alphabets),end=" ")
     alphabets+=1
    print()
