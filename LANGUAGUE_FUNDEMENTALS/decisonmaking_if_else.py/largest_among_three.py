# number largest among 3
num1 = int(input("type number"))
num2 = int(input("type number"))
num3 = int(input("type number"))
if (num1 > num2 and num1 > num3):
    print(f"{num1} is greatest")
elif (num2 > num1 and num2 > num3):
    print(f"{num2} is greatest")
elif (num3 > num1 and num3 > num2):
    print(f"{num3} is greatest")
elif (num1 == num2 and num1 == num3):
    print("equel")

