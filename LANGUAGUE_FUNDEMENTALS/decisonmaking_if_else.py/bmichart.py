print("welcome to the bmi calculator")
weight_in_kg=int(input("what is your weight in kg"))
height_in_cm=int(input("what is your height in cm "))
height_in_m=(height_in_cm/100)
bmi=(weight_in_kg/height_in_m**2)
print(f"your bmi {bmi} is")
if bmi < 19:
    print("you are underweight..please eat well")
elif  bmi< 25:
    print("you are healthy..keep going")
elif  bmi <30:
    print(" you are overweight...please control your food")
elif  bmi <40:
    print("you are obesity..please...take care..take proper diet.")
else:
    print("you are sever obese..take apropriat action")