# 1.Write a python program to convert the temperature in degree centigrade to fahrenheit

temp_in_c=float(input("enter your temp in degree c"))
temp_in_fahrenheit=((temp_in_c * 9/5)+32)
print(f"your {temp_in_c} degree c in fahrenheit is {temp_in_fahrenheit}")


# 2. Write a python program to find compound interest


principal_P=float(input("enter principal amount P :"))# loan taken amount
interest_r=float(input("enter your interest rate r :"))# inrest rate
time_duration_t=float(input("enter your duration of time in years t :"))#duration/year
n=float(input("no of times inerest get compounded anually n:"))#in year or month or days or semi anually,quterly
final_amount_A=principal_P * ((1 + interest_r/100*n)**(n*time_duration_t))# total pay amount

Compound_interest_CI=final_amount_A - principal_P# compound intrest rate

print(f"your compound interest is {Compound_interest_CI} and your final pay amount is {final_amount_A}")


# 3. Write a python program to find area of a circle.
radius_r=float(input("enter your area r in meter"))
area_A=(3.14 * radius_r**2)
print(f"area of circle is {area_A}")

# or 
# this a etc references knoweledge
# import math is mathematical function so we get pi value, pi value is not already not in there so so we import
import math
radius_r=float(input("enter your area r in meter"))
area_A=(math.pi * radius_r**2)
print(f"area of circle is {area_A}")
