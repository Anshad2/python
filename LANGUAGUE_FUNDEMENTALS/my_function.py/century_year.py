# century year
def century_year(year):
    
  year=True if year%100==0 else not False
  return year
print(century_year(2000))


# leap year(year)
# factorial(num)
# is prime(num)
# is_amstrong(number)

# leap year
def leap_year(year):
   if year % 400==0 and year%100==0 or year % 4==0 and year%100!=0:
     return True
   else:
     return False
print(leap_year(2016))

# 
def factrial_num(num):
  fact=1
  for num in range(1,num+1):
   fact=fact*num
  return fact
print(factrial_num(5))

# is prime
def is_prime(num):
  is_prime=True
  for i in range(2,num):
     if (num%i==0):
       is_prime=False
       break
  return is_prime  
print(is_prime(17))


# amstrong number
def is_amstrong(num):
 digit_count=len(num)
 num=int(num)
 original=num
 sum=0
 while(num!=0):
   last_digit=num %10
   pow=last_digit**digit_count
   sum=sum+pow
   num=num//10
 return (True if sum==original else False)
print(is_amstrong("153"))



