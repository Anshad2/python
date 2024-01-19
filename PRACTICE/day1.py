
# 1.Write a program to display ‘’HELLO’’ if a number entered by user is a multiple of five,
#  otherwise print ‘’Bye’’.
# num=int(input("eneter your number"))

# if num%5==0:
#  print("HELLO")
# else:
#  print("Bye")

# # 2.Write a program to check whether a person is eligible for voting or not

# age=int(input("please eneter your age"))
# if age>=18:
#   print("you are eligible for vote")
# else:
#   print("sorry your not eligible for vote...wait untill you become 18 ")

# 3.Write a program to accept percentage from the user and display the grade according to the following 
# criteria:
# Mark > 90 =A Grade
# >80 and <= 90 = B Grade
# >=60 and <= 80 =C Grade
# Below 60 = D grade

# mark=int(input("eneter yor mark"))
# if mark >90:
#    print("A Grade")
# elif mark > 80 and mark <=90:
#    print("B Grade")
# elif mark >=60 and mark <=80:
#    print("C Grade")
# else:
#    print("D Grade")

# 4.Write a program to find the largest number out of three numbers excepted from user.


num1=int(input("eneter your number"))
num2=int(input("enter your number"))
num3=int(input("enter your number"))

if (num1>num2 and num1>num3):
    print(f"{num1} is largest")
elif (num2>num1 and num2>num3):
    print(f"{num2} is the largest")
elif (num3>num1 and num3>num2):
    print(f"{num3} is the largest")
elif (num1==num2 and num1==num3):
    print("equel")




