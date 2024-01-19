age=25 # int
# type
print(type(age))

name="anshad" # string
print(type(name))

is_vaccinated=True # boolean= True or False
print(type(is_vaccinated))

total=123.567 # float
print(type(total))


fh=int(input("enter the value"))
deg=(fh-32)*(5/9)
print(f"{fh} fh is equel to {deg} degree")

# 
selling_prize=int(input("enter the selling price"))
cost_prize=int(input("enter the value of cost prize"))
profit=selling_prize-cost_prize
print(f"the profit is {profit}")
profit_in_percentage=(profit/cost_prize)*100
print(f"the profit percentage is {profit_in_percentage}")

# calculate bmi
height_in_cm=int(input("enter the value in cm"))
weight_in_kg=int(input("enter weight in kg"))
height_in_meter=(height_in_cm/100)
bmi=(weight_in_kg/height_in_meter**2)
print(f"your bmi is {bmi}")

# electricity_bill

unit=int(input("enter the unit consumed"))
rate_per_unit=15
pay_amount=(unit*rate_per_unit)
print(f"your electricity bill is {pay_amount}")
                                   

# fuel efficiency
total_distance_in_kilometer=int(input("enter the distance covered in kilometer"))
total_petrol_consumed=int(input("enter number of litre consumed"))
fuel_efficiency=(total_distance_in_kilometer/total_petrol_consumed)
print(f"the fuel efficiency of yor vehicle is {fuel_efficiency}")



