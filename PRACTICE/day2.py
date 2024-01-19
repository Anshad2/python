# 1.Write a program to accept two numbers and mathematical operators and perform operation accordingly
# Output:
# Enter 1st number :10
# Enter 2nd number:5
# Enter operator: -
# The answer:5

# num1=int(input("enter 1st number"))
# num2=int(input("enter the 2nd number"))
# sub_res=(num1-num2)
# print(f"the answer is : {sub_res}")


# 2. Take input of age of 3 people by user and determine oldest and youngest among them.

person1_age=int(input("enter your age;"))
person2_age=int(input("enter your age;"))
person3_age=int(input("enter your age;"))
if person1_age>person2_age and person1_age>person3_age:
    print(f"{person1_age}  is oldest")
elif person2_age>person1_age and person2_age>person3_age:
    print(f"{person2_age} is oldest")
else:
    print(f"{person3_age} is oldest")
if person1_age<person2_age and person1_age<person3_age:
    print(f"{person1_age} is youngest")
elif person2_age<person1_age and person2_age<person3_age:
    print(f"{person2_age} is youngest")
else:
     print(f"{person3_age} is youngest")

# by using min and max
# person1=int(input("enter your age"))
# person2=int(input("enter your age"))
# person3=int(input("enter your age"))

# oldest=max(person1,person2,person3)
# youngest=min(person1,person2,person3)
# print(f"the oldest person is {oldest} year old")
# print(f"the youngest person is {youngest} year old")




# 3. Take values of length and breadth of a rectangle from user and check if it is square or not.
# length=float(input("enter the length of rectangle"))
# breadth=float(input("enter the breadth of rectangle"))
# print("rectangle is square" if length==breadth else "rectangle is not a square")