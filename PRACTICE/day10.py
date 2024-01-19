
# 1. Write a Python program that ask users to enter a number and keep asking the users to enter a correct
#  number until the number with in the range that we given

start_range = 1
end_range = 10

for i in range(3):    
    user_input = int(input(f"Please enter a number between {start_range} and {end_range}: "))
    if start_range <= user_input <= end_range:
        print(f"You entered: {user_input} which is given range")
        break  
    else:
        print(f"Number should be between {start_range} and {end_range}. Try again. ")


        # or
    
start=int(input("start number"))
end_num=int(input("enter number"))
while(True):
    user_input=int(input("enter input"))
    if start<=user_input<=end_num:
        print("here we go.......")
        break
        

# 2.Write a python program to list the even numbers from the range that given by the user and delete
#  the multiplication of 5 from the list

user_input_range=int(input("enter the start number"))
end_number_range=int(input("enter the end range"))
for i in range(user_input_range,end_number_range):
  if i % 2==0 and i % 5 !=0:
     print(i)

# 3.Pattern print 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     *
num=int(input("row"))# no of rows
for i in range(num):#row
    for j in range(num-i-1):#spaces
        print("",end=" ")
    for j in range(i+1):#coloumn
     print("*",end=" ")
    print()
for i in range(num,0,-1):#row
    for j in range(0,num-i):#space
        print(end=" ")
    for j in range(0,i):#coloumn
        print("*",end=" ")
    print()