
start_year=int(input("year"))
end_year=2023
while(start_year<=end_year):
    if start_year % 400==0 and start_year % 100==0 or start_year % 4==0 and start_year%100!=0:
     print(start_year)
    start_year+=1
    
# 
def leap_year(year):
   if year%400==0:
      if year%100==0:
         if year%4==0:
            return True
         return True
      return True
   else:
      return False
print(leap_year(1900))

# 
def leap_year(year):
   if year%400==0 and year%100==0 or year%100!=0 and year%4==0:
         return True
   else:
      return False
print(leap_year(1900))