# 1. Write a Python program to find leap year (user input)
year=int(input("what is your year"))
if year % 400 == 0 and year%100==0 or year%4==0 and year% 100!=0:
 print(f"the year {year} is  leap year year ")
else:
 print(f"the year {year} is not a leap year")
    
# 2.Write a python program to sum all the items in the dictionary 
my_dict={"a":1000,"b":2000,"c":4000,"d":5000,"e":2300}
sum=0
for i in my_dict:
 sum=sum+my_dict[i]
print(sum)


# 3.Pattern print 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

for i in range(1,6):
 for j in range(5):
  print("*",end=" ")
 print()