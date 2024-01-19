# 1.Write a program to print 10,8,6,4,2,0,-2,-4,-6,-8,-10

# using for loop
for i in range(10,-11,-2):
    print(i)

# using while loop
i=10
while(i>=-10):
  print(i)
  i-=2

# 2. Write a program to print sum of even number in a range

#using for loop
sum=0
for i in range(2,51):
  if i % 2==0:
    sum=sum+i
print(f"sum of all even numbers in a range 2 to 50 is {sum}" )

#using while loop

sum = 0
i = 2
while i <= 50:
  if i % 2 == 0:
    print(i)
    sum+=i
  i+=1
print(f"Sum of all the even numbers range from 2 to 50 is {sum}")
    

# 3. Write a program to calculate BMI and give message ‘’over weight,underweight,healthy’’
print("welcome to the BMI calculator...")
height_in_cm=int(input("enter your height in cm"))
weight_in_kg=int(input("enter your height in kg"))
height_in_meter=(height_in_cm/100)
BMI=int(weight_in_kg/height_in_meter**2)
print(f"your bmi is {BMI}")

if BMI < 19:
    print("you are underweight..please eat well")
elif  BMI < 25:
    print("you are healthy..keep going")
elif  BMI <30:
    print(" you are overweight...please control your food")
elif  BMI <40:
    print("you are obesity..please...take care..take proper diet.")
else:
    print("you are sever obese..take apropriat action")
