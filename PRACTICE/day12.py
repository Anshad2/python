# 1. Write a Python program that keep on accepting number from the user until users enter zero display 
# the sum of all number

sum=0
while True:
    user_input=int(input("enter number"))
    if user_input==0:
        break
    sum=sum+user_input
print(f"the sum of all numbers is {sum}")
   

# 2.Write a python program to accept decimal number and display it’s binary number
decimal=int(input("enter numbr : "))
binary=""
while decimal>0:
   remainder=decimal % 2
   binary=str(remainder)+binary
   decimal=decimal //2
print(f" the binary of {decimal} is {binary}")

# eg: 13/2=1 6,rem=1
# 6/2=3 rem=0
# 3/2=1 rem=1
# 1/2=0 rem1
# write in reverse order


# 3.Pattern print 
# 6 6 6 6 6 6 
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1
n=6
for i in range(n,0,-1):
    for j in range(0,i):
     print(i,end=" ")
    print()
