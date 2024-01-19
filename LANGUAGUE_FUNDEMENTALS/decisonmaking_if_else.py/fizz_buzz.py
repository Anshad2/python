# fizz_buzz interview question
# num = int(input("what is your number"))
# if num % 15 == 0 :
#     print("fizz_buzz")
# elif num % 5== 0:
#     print("buzz")
# elif num % 3 == 0:
#  print("fizz")
# else:
#    print("========")

    
for num in range(1,101):
   if num % 3==0 and num % 5 ==0:
      print("fizz_buzz")
   elif num % 3==0:
      print("fizz")
   elif num% 5==0:
      print("buzz")
   else:
      print(num)
      
