# sorted order or increasing or decreasing
num1 = int(input("what is your 1st number"))
num2 = int(input("what is your 2nd number"))
num3 = int(input("what is your 3rd number"))
if num1 > num2 and num1 > num3:
    if num2>num3:
        print(num1,num2,num3)
    else:
        print(num1,num3,num2)
elif num2>num1 and num2>num3:
     if (num1>num3):
         print(num2,num1,num3)
     else:
         print(num2,num3,num1)
elif num3>num1 and num3>num2:
    if num1>num2:
        print(num3,num1,num2)
    else:
        print(num3,num2,num1)
    