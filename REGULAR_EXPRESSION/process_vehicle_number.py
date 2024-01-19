from re import *
f=open("C:\\Users\\user\\Desktop\\my python\\Regular_expression\\vehicle_numbers.txt","r")
rule="((KL)|(TN)){1}(-)?\d{2}(-)?[A-Z]{1,2}(-)?\d{4}"
for line in f:
    vehicle_number=line.rstrip("\n")
    matcher=fullmatch(rule,vehicle_number)
    if matcher!=None:
        print(vehicle_number)




