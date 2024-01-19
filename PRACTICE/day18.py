#  The original list : [1, 3, 5, 1, 3, 2, 5, 4, 2] (user input)
# Matrix after grouping : [[1, 1], [2, 2], [3, 3], [4], [5, 5]]

user_input_lst=[1, 3, 5, 1, 3, 2, 5, 4, 2]
res = []

for i in user_input_lst:
	correct = False
	for j in range(len(res)):
		if i in res[j]:
			res[j].append(i)
			correct = True
			break
	if not correct:
		res.append([i])
print("Matrix after grouping : " + str(res))

# 2.Write a program to calculate the electricity bill. Accept the number of units consumed from the user
# Unit                        Price
# First 100 units      No charge
# Next 100 units     Rs 5 per unit
# After 200 units    Rs 10 per unit
# For example if input unit is 350 then total bill amount is Rs 2000

print("Welcome to the electricity bill calcuator ....here we go : ")

unit_consumed=float(input("enter the unit consumed : "))
if unit_consumed<=100:
	total_bill=0
   
elif unit_consumed<=200:
    total_bill=float(unit_consumed)*5
else:
    total_bill=float(unit_consumed)*10
print(f"your total electricity bill is {total_bill}")




#        3. Pattern print 
#       A 
#      A B 
#     A B C 
#    A B C D 
#   A B C D E
def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(i):
            print(chr(65 + j), end=" ")  
        print()
print_pattern(5) 
