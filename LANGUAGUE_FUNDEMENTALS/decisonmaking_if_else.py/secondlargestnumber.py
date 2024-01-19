# second largest number
num1 = int(input("type your number"))
num2 = int(input("type your number"))
num3 = int(input("type your number"))
if num1 > num2 and num2>num3:
    if num2>num3:
     print(f"num2 {num2} second largest")
    else:
     print(f"num3 {num3} second largest")
elif (num2 > num1 and num2 > num2):
  if num1>num3:
    print(f"num1 is {num1} is the second largest")
  else:
    print(f"num3 is {num3} ia the largest number")
elif (num3 > num1 and num3 > num2):
  if  num1 > num2:
    print(f"num1 is {num1} is second largest")
  else:
    print(f"num2 is {num2} is second largest")





# sorted order